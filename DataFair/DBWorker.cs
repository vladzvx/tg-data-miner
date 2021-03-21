﻿using Npgsql;
using System;
using System.Collections.Concurrent;
using System.Threading;
using Common;
using System.Threading.Tasks;

namespace DataFair
{
    public class DBWorker
    {
        private readonly ConcurrentQueue<Message> messages = new ConcurrentQueue<Message>();
        private readonly ConcurrentQueue<Entity> entities = new ConcurrentQueue<Entity>();

        private readonly NpgsqlConnection StreamReadConnection;
        private readonly NpgsqlConnection ReadConnention;
        private readonly NpgsqlConnection WriteConnention;
        private readonly NpgsqlCommand CheckUser;
        private readonly NpgsqlCommand CheckChat;
        private readonly NpgsqlCommand GetChatsForUpdate;
        private readonly NpgsqlCommand SetChatChecked;

        private readonly object ReadLocker = new object();
        private readonly object StreamReadLocker = new object();
        private readonly object WriteLocker = new object();
        private readonly string ConnectionString;
        private readonly Thread MessagesWritingThread;
        private readonly Thread UsersWritingThread;
        private readonly CancellationTokenSource CancellationTokenSource = new CancellationTokenSource();

        public DBWorker(string connectionString)
        {
            this.ConnectionString = connectionString;
            ReadConnention = new NpgsqlConnection(ConnectionString);
            ReadConnention.Open();
            WriteConnention = new NpgsqlConnection(ConnectionString);
            WriteConnention.Open();
            StreamReadConnection = new NpgsqlConnection(ConnectionString);
            StreamReadConnection.Open();
            MessagesWritingThread = new Thread(new ParameterizedThreadStart(MessagesWriter));
            MessagesWritingThread.Start(CancellationTokenSource.Token);
            UsersWritingThread = new Thread(new ParameterizedThreadStart(UsersWriter));
            UsersWritingThread.Start(CancellationTokenSource.Token);

            CheckUser = ReadConnention.CreateCommand();
            CheckUser.CommandType = System.Data.CommandType.StoredProcedure;
            CheckUser.CommandText = "check_user";
            CheckUser.Parameters.Add(new NpgsqlParameter("user_id", NpgsqlTypes.NpgsqlDbType.Bigint));

            CheckChat = ReadConnention.CreateCommand();
            CheckChat.CommandType = System.Data.CommandType.StoredProcedure;
            CheckChat.CommandText = "check_chat";
            CheckChat.Parameters.Add(new NpgsqlParameter("chat_id", NpgsqlTypes.NpgsqlDbType.Bigint));

            GetChatsForUpdate = StreamReadConnection.CreateCommand();
            GetChatsForUpdate.CommandType = System.Data.CommandType.StoredProcedure;
            GetChatsForUpdate.CommandText = "get_unupdated_chats";
            GetChatsForUpdate.Parameters.Add(new NpgsqlParameter("dt", NpgsqlTypes.NpgsqlDbType.Timestamp));

            SetChatChecked = WriteConnention.CreateCommand();
            SetChatChecked.CommandType = System.Data.CommandType.StoredProcedure;
            SetChatChecked.CommandText = "set_chat_checked";
            SetChatChecked.Parameters.Add(new NpgsqlParameter("_chat_id", NpgsqlTypes.NpgsqlDbType.Bigint));
        }

        public void SetChatUpdated(long id)
        {
            lock (WriteLocker)
            {
                SetChatChecked.Parameters["_chat_id"].Value = id;
                SetChatChecked.ExecuteNonQuery();
            }
        }
        public void Stop()
        {
            ReadConnention.Dispose();
            WriteConnention.Dispose();
            CancellationTokenSource.Cancel();
        }

        private static void WriteSingleMessage(NpgsqlCommand command, Message message)
        {
            command.Parameters["_message_timestamp"].Value = message.Timestamp.ToDateTime();
            command.Parameters["_message_id"].Value = message.Id;
            command.Parameters["_chat_id"].Value = message.ChatId;
            command.Parameters["_user_id"].Value = message.FromId!=0? message.FromId :DBNull.Value;
            command.Parameters["_reply_to"].Value = message.ReplyTo != 0 ? message.ReplyTo : DBNull.Value;
            command.Parameters["_thread_start"].Value = message.ThreadStart != 0 ? message.ThreadStart : DBNull.Value;
            command.Parameters["_media_group_id"].Value = message.MediagroupId != 0 ? message.MediagroupId : DBNull.Value;
            command.Parameters["_forward_from_id"].Value = message.ForwardFromId != 0 ? message.ForwardFromId : DBNull.Value;
            command.Parameters["_forward_from_message_id"].Value = message.ForwardFromMessageId != 0 ? message.ForwardFromMessageId : DBNull.Value;
            command.Parameters["_text"].Value = message.Text;
            command.Parameters["_media"].Value = DBNull.Value;// essage.Media;
            command.Parameters["_formatting"].Value = DBNull.Value;// message.Formating;
            command.ExecuteNonQuery();
        }

        private static void WriteSingleUser(NpgsqlCommand command, Entity entity)
        {
            command.Parameters["_user_id"].Value = entity.Id;
            command.Parameters["sender_username"].Value = entity.Link;
            command.Parameters["sender_first_name"].Value = entity.FirstName;
            command.Parameters["sender_last_name"].Value = entity.LastName;
            command.ExecuteNonQuery();
        }

        private static void WriteSingleEntity(NpgsqlCommand command, Entity entity)
        {
            command.Parameters["_chat_id"].Value = entity.Id;
            command.Parameters["_username"].Value = entity.Link.Equals(string.Empty)? DBNull.Value: entity.Link;
            command.Parameters["_title"].Value = entity.FirstName;
            command.Parameters["pair_chat_id"].Value = entity.PairId!=0?entity.PairId:DBNull.Value;
            command.Parameters["_is_group"].Value = entity.Type==EntityType.Group;
            command.Parameters["_is_channel"].Value = entity.Type==EntityType.Channel;
            command.ExecuteNonQuery();
        }

        private void MessagesWriter(object cancellationToken)
        {
            NpgsqlConnection Connention = new NpgsqlConnection(ConnectionString);
            Connention.Open();
            NpgsqlCommand command = Connention.CreateCommand();
            command.CommandType = System.Data.CommandType.StoredProcedure;
            command.CommandText = "add_message";
            command.Parameters.Add(new NpgsqlParameter("_message_timestamp", NpgsqlTypes.NpgsqlDbType.Timestamp));
            command.Parameters.Add(new NpgsqlParameter("_message_id", NpgsqlTypes.NpgsqlDbType.Bigint));
            command.Parameters.Add(new NpgsqlParameter("_chat_id", NpgsqlTypes.NpgsqlDbType.Bigint));
            command.Parameters.Add(new NpgsqlParameter("_user_id", NpgsqlTypes.NpgsqlDbType.Bigint));
            command.Parameters.Add(new NpgsqlParameter("_reply_to", NpgsqlTypes.NpgsqlDbType.Bigint));
            command.Parameters.Add(new NpgsqlParameter("_thread_start", NpgsqlTypes.NpgsqlDbType.Bigint));
            command.Parameters.Add(new NpgsqlParameter("_media_group_id", NpgsqlTypes.NpgsqlDbType.Bigint));
            command.Parameters.Add(new NpgsqlParameter("_forward_from_id", NpgsqlTypes.NpgsqlDbType.Bigint));
            command.Parameters.Add(new NpgsqlParameter("_forward_from_message_id", NpgsqlTypes.NpgsqlDbType.Bigint));
            command.Parameters.Add(new NpgsqlParameter("_text", NpgsqlTypes.NpgsqlDbType.Text));
            command.Parameters.Add(new NpgsqlParameter("_media", NpgsqlTypes.NpgsqlDbType.Jsonb));
            command.Parameters.Add(new NpgsqlParameter("_formatting", NpgsqlTypes.NpgsqlDbType.Jsonb));

            CancellationToken Token = (CancellationToken)cancellationToken;
            while (!Token.IsCancellationRequested)
            {
                try
                {
                    while (!messages.IsEmpty)
                    {
                        using (NpgsqlTransaction transaction = Connention.BeginTransaction())
                        {
                            try
                            {
                                int count = 0;
                                for (int i = 0; i < 10000 && !messages.IsEmpty; i++)
                                {
                                    if (messages.TryDequeue(out Message message))
                                    {
                                        WriteSingleMessage(command, message);
                                        count++;
                                    }
                                }
                                transaction.Commit();
                            }
                            catch (Exception ex)
                            {
                                transaction.Rollback();
                                throw ex;
                            }
                        }
                    }
                    Thread.Sleep(300);
                }
                catch (Exception ex)
                {
                    //logger.Error(ex, "Error while DB writing to DB");
                }



            }

            Connention.Close();
            Connention.Dispose();
        }

        private void UsersWriter(object cancellationToken)
        {
            NpgsqlConnection Connention = new NpgsqlConnection(ConnectionString);
            Connention.Open();
            NpgsqlCommand command1 = Connention.CreateCommand();
            command1.CommandType = System.Data.CommandType.StoredProcedure;
            command1.CommandText = "add_user"; ;
            command1.Parameters.Add(new NpgsqlParameter("_user_id", NpgsqlTypes.NpgsqlDbType.Bigint));
            command1.Parameters.Add(new NpgsqlParameter("sender_username", NpgsqlTypes.NpgsqlDbType.Text));
            command1.Parameters.Add(new NpgsqlParameter("sender_first_name", NpgsqlTypes.NpgsqlDbType.Text));
            command1.Parameters.Add(new NpgsqlParameter("sender_last_name", NpgsqlTypes.NpgsqlDbType.Text));

            NpgsqlCommand command2 = Connention.CreateCommand();
            command2.CommandType = System.Data.CommandType.StoredProcedure;
            command2.CommandText = "add_chat"; ;
            command2.Parameters.Add(new NpgsqlParameter("_chat_id", NpgsqlTypes.NpgsqlDbType.Bigint));
            command2.Parameters.Add(new NpgsqlParameter("_title", NpgsqlTypes.NpgsqlDbType.Text));
            command2.Parameters.Add(new NpgsqlParameter("_username", NpgsqlTypes.NpgsqlDbType.Text));
            command2.Parameters.Add(new NpgsqlParameter("pair_chat_id", NpgsqlTypes.NpgsqlDbType.Bigint));
            command2.Parameters.Add(new NpgsqlParameter("_is_group", NpgsqlTypes.NpgsqlDbType.Boolean));
            command2.Parameters.Add(new NpgsqlParameter("_is_channel", NpgsqlTypes.NpgsqlDbType.Boolean));

            CancellationToken Token = (CancellationToken)cancellationToken;
            while (!Token.IsCancellationRequested)
            {
                try
                {
                    while (!entities.IsEmpty)
                    {
                        using (NpgsqlTransaction transaction = Connention.BeginTransaction())
                        {
                            try
                            {
                                int count = 0;
                                for (int i = 0; i < 10000 && !entities.IsEmpty; i++)
                                {
                                    if (entities.TryDequeue(out Entity entity))
                                    {
                                        switch (entity.Type)
                                        {
                                            case EntityType.User:
                                                WriteSingleUser(command1, entity);
                                                break;
                                            case EntityType.Group:
                                            case EntityType.Channel:
                                                WriteSingleEntity(command2, entity);
                                                break;

                                        }
                                        
                                        count++;
                                    }
                                }
                                transaction.Commit();
                            }
                            catch (Exception ex)
                            {
                                transaction.Rollback();
                                throw ex;
                            }
                        }
                    }
                    Thread.Sleep(300);
                }
                catch (Exception ex)
                {
                    //logger.Error(ex, "Error while DB writing to DB");
                }



            }

            Connention.Close();
            Connention.Dispose();
        }


        public void PutEntity(Entity entity)
        {
            entities.Enqueue(entity);
        }
        public void PutMessage(Message message)
        {
            messages.Enqueue(message);
        }

        public void GetUnudatedChats(DateTime BoundDateTime)
        {
            GetChatsForUpdate.Parameters["dt"].Value = BoundDateTime;
            NpgsqlDataReader reader = GetChatsForUpdate.ExecuteReader();
            while (reader.Read())
            {
                try
                {
                    long ChatId = reader.GetInt64(0);
                    long PairId = reader.IsDBNull(1) ? 0 : reader.GetInt64(1);
                    long Offset = reader.GetInt64(2);
                    DateTime LastUpdate = reader.IsDBNull(3) ? DateTime.MinValue : reader.GetDateTime(3);
                    bool PairChecked = reader.IsDBNull(4) ? true : reader.GetBoolean(4);
                    string Username = reader.IsDBNull(5) ? string.Empty : reader.GetString(5);
                    string PairUsername = reader.IsDBNull(6) ? string.Empty : reader.GetString(6);

                    Order order = new Order() { Id = ChatId, Link = Username, Offset = Offset, PairId = PairId, PairLink = PairUsername };
                    if (!PairChecked)
                    {
                        order.Type = OrderType.GetFullChannel;
                        Storage.Orders.Enqueue(order);
                    }
                    else
                    {
                        order.Type = OrderType.History;
                        Storage.Orders.Enqueue(order);
                    }
                }
                catch (InvalidCastException) { }
            }
            reader.Close();
        }
        public async Task<bool> CheckEntity(Entity entity)
        {
            lock (ReadLocker)
            {
                switch (entity.Type)
                {
                    case EntityType.User:
                        {
                            CheckUser.Parameters["user_id"].Value = entity.Id;
                            using (NpgsqlDataReader reader = CheckUser.ExecuteReader())
                            {
                                while (reader.Read())
                                {
                                    try
                                    {
                                        return reader.GetBoolean(0);
                                    }
                                    catch (InvalidCastException) { }

                                }
                                reader.Close();
                            }
                            break;
                        }
                    default:
                        {
                            CheckChat.Parameters["chat_id"].Value = entity.Id;
                            using (NpgsqlDataReader reader = CheckChat.ExecuteReader())
                            {
                                while (reader.Read())
                                {
                                    try
                                    {
                                        return reader.GetBoolean(0);
                                    }
                                    catch (InvalidCastException) { }

                                }
                                reader.Close();
                            }
                            break;
                        }

                }
            }
            
            return false;
        }
    }
}
