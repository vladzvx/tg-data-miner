﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Telegram.Bot.Types;

namespace Bot.Core.Interfaces.BotFSM
{
    public interface IRightChecker
    {
        public Task<bool> Check<TBot>(Update update, Services.Bot.FSM<TBot> fsm) where TBot:IConfig,new();
    }
}
