﻿using Common;
using MongoDB.Bson;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Channels;
using Telegram.Bot;
using Telegram.Bot.Types;
using Telegram.Bot.Types.Enums;
using Telegram.Bot.Types.ReplyMarkups;

namespace Bot.Core.Models
{
    public class Page
    {
        public const int PageMaxSize = 1500;
        public static Page Empty = new Page(ObjectId.Empty) { position = Position.Empty };


        public enum Position
        {
            First,
            Middle,
            Last,
            Single,
            Empty
        }

        public Position position { get; set; }
        public ObjectId Id { get; private set; }
        public ObjectId? NextId { get; private set; }
        public ObjectId? PreviousId { get; private set; }

        public int Number;
        public string Text { get; set; } = string.Empty;
        public List<MessageEntity> Formatting { get; set; } = new List<MessageEntity>();
        public int offset { get; set; } = 0;
        public int count { get; set; } = 0;



        public List<SearchResult> results = new List<SearchResult>();
        public Page(ObjectId id, ObjectId? previousId=null, ObjectId? nextId=null)
        {
            this.Id = id;
            this.NextId = nextId;
            this.PreviousId = previousId;
        }
        public bool TryAddResult(SearchResult res)
        {
            if (Text.Length < PageMaxSize)
            {
                string line = count.ToString() + ". " + (res.Text.Length > 100 ? res.Text.Substring(0, 99) + "..." : res.Text) + "\n\n";

                MessageEntity formatting = new MessageEntity() { Length = count.ToString().Length, Url = res.Link, Offset = offset, Type = MessageEntityType.TextLink };
                offset += line.Length;
                count++;
                Text += line;
                Formatting.Add(formatting);
                res.Page = this.Number;
                return true;
            }
            else
            {
                return false;
            }
        }

        public TextMessage GetTextMessage(ITelegramBotClient client, long chatId, Channel<int> channel=null)
        {
            InlineKeyboardButton Next = new InlineKeyboardButton();
            Next.Text = "Далее";
            Next.CallbackData = NextId.HasValue ? NextId.Value.ToString() : string.Empty;

            InlineKeyboardButton Prev = new InlineKeyboardButton();
            Prev.Text = "Назад";
            Prev.CallbackData = PreviousId.HasValue ? PreviousId.Value.ToString() : string.Empty;

            if ((Text.Length <= PageMaxSize) && !(position == Position.Last))
            {
                position = Position.Single;
            }

            InlineKeyboardMarkup keyb;
            if (position == Position.First)
            {
                keyb = new InlineKeyboardMarkup(Next);
            }
            else if (position == Position.Middle)
            {
                keyb = new InlineKeyboardMarkup(new InlineKeyboardButton[2] { Prev, Next });
            }
            else if (position == Position.Last)
            {
                keyb = new InlineKeyboardMarkup(Prev);
            }
            else if (position==Position.Single)
            {
                keyb = null;
            }
            else
            {
                keyb = null;
            }
            return new TextMessage(client, chatId, Text, channel, new ReplyKeyboardRemove(), formattings: new List<MessageEntity>(Formatting),
                inlineKeyboard: keyb);
        }

        public EditTextMessage GetEditTextMessage(ITelegramBotClient client, long chatId,int messageId, Channel<int> channel = null)
        {
            InlineKeyboardButton Next = new InlineKeyboardButton();
            Next.Text = "Далее";
            Next.CallbackData = NextId.HasValue ? NextId.Value.ToString() : string.Empty;

            InlineKeyboardButton Prev = new InlineKeyboardButton();
            Prev.Text = "Назад";
            Prev.CallbackData = PreviousId.HasValue ? PreviousId.Value.ToString() : string.Empty;

            InlineKeyboardMarkup keyb;


            if (position == Position.First)
            {
                keyb = new InlineKeyboardMarkup(Next);
            }
            else if (position == Position.Middle)
            {
                keyb = new InlineKeyboardMarkup(new InlineKeyboardButton[2] { Prev, Next });
            }
            else if (position == Position.Last)
            {
                keyb = new InlineKeyboardMarkup(Prev);
            }
            else
            {
                keyb = null;
            }
            return new EditTextMessage(client, chatId, Text, messageId, channel, new ReplyKeyboardRemove(), formattings: new List<MessageEntity>(Formatting),
                inlineKeyboard: keyb);
        }
    }
}
