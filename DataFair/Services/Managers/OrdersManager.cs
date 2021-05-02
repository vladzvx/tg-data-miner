﻿using Common;
using DataFair.Services.Interfaces;
using Microsoft.Extensions.Hosting;
using Npgsql;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Timers;

namespace DataFair.Services
{
    public class OrdersManager:IHostedService
    {
        
        private System.Timers.Timer timer = new System.Timers.Timer(Options.OrderGenerationTimerPeriod);
        private static NLog.Logger logger = NLog.LogManager.GetCurrentClassLogger();
        private readonly State state;
        private readonly OrdersGenerator ordersGenerator;
        private readonly CancellationTokenSource cts = new CancellationTokenSource();
        private readonly object sync = new object();
        private readonly LoadManager manager;
        private bool GenerationOn = false;
        public OrdersManager(State state, OrdersGenerator ordersGenerator, LoadManager manager)
        {
            this.state = state;
            this.ordersGenerator = ordersGenerator;
            timer.Elapsed += TimerAction;
            this.manager = manager;
        }

        private void TimerAction(object sender,ElapsedEventArgs args)
        {   
            if (GenerationOn&&state.Orders.Count==0&&Monitor.TryEnter(sync))
            {
                try
                {
                    Task.WaitAll(ordersGenerator.CreateHistoryLoadingOrders());//, CreateGetFullChannelOrders());
                }
                catch { }
                Monitor.Exit(sync);
            }
            //manager.AddValue();
        }

        public Task StartAsync(CancellationToken cancellationToken)
        {
            timer.Start();
            return Task.CompletedTask;
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
            timer.Stop();
            cts.Cancel();
            return Task.CompletedTask;
        }
    }
}
