﻿using Common;
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Timers;

namespace DataFair
{
    struct CachedEntityInfo
    {
        public CachedEntityInfo(long Offset)
        {
            this.Offset = Offset;
            LastTimeMessage = DateTime.UtcNow;
        }
        public long Offset;
        public DateTime LastTimeMessage;
    }

    internal static class Storage
    {
        internal static Timer timer = new Timer(20000);
        internal static DBWorker worker = new DBWorker(Environment.GetEnvironmentVariable("ConnectionString"));


        public static ConcurrentQueue<Order> Orders = new ConcurrentQueue<Order>();
        public static ConcurrentBag<SessionSettings> Sessions = new ConcurrentBag<SessionSettings>();
        public static ConcurrentBag<Common.Collector> Collectors = new ConcurrentBag<Collector>();
        public static ConcurrentBag<Common.User> Users = new ConcurrentBag<User>();

        public static ConcurrentDictionary<long, CachedEntityInfo> Chats = new ConcurrentDictionary<long, CachedEntityInfo>();

        private static object sync = new object();
        static Storage()
        {
            using (ApplicationContext db = new ApplicationContext())
            {
                foreach (SessionSettings session in db.Sessions.ToList())
                {
                    Sessions.Add(session);
                }
                foreach (Collector collector in db.Collectors.ToList())
                {
                    Collectors.Add(collector);
                }
                foreach (User user in db.Users.ToList())
                {
                    Users.Add(user);
                }
            }

            timer.Elapsed += action;
            timer.AutoReset = true;
            timer.Start();
        }

        private static void action(object sender, ElapsedEventArgs args)
        {
            if (System.Threading.Monitor.TryEnter(sync))
            {
                worker.GetUnupdatedChats(DateTime.UtcNow.AddHours(-24));
                System.Threading.Monitor.Exit(sync);
            }
        }
    }
}
