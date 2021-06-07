﻿using Common;
using DataFair.Services;
using DataFair.Services.DataBase.DataProcessing;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace DataFair.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class CommandController
    {
        private readonly OrdersGenerator ordersGenerator;
        private readonly State state;
        private readonly DoubledValuesFinder finder;
        private readonly DoubledValuesKiller killer;
        //private readonly CancellationToken token;

        public CommandController(OrdersGenerator ordersGenerator, State state, DoubledValuesFinder finder, DoubledValuesKiller killer)
        {
            this.ordersGenerator = ordersGenerator;
            this.state = state;
            this.finder = finder;
            this.killer = killer;
            //this.token = token;
        }

        [HttpPost("GetFullChannel")]
        [EnableCors()]
        public string PostRequest()
        {
            ordersGenerator.CreateGetFullChannelOrders(800).Wait();
            return "ok";
            
        }

        [HttpPost("PostEmptyOrder")]
        [EnableCors()]
        public string PostEmptyOrder()
        {
            state.Orders.Enqueue(new Order() { Type = OrderType.Empty });
            return "ok";

        }

        [HttpPost("GetGroupsHistory")]
        [EnableCors()]
        public string PostRequest2()
        {
            ordersGenerator.CreateGroupHistoryLoadingOrders().Wait();
            return "ok";

        }

        [HttpPost("GetHistory")]
        [EnableCors()]
        public string PostRequest3()
        {
            ordersGenerator.CreateHistoryLoadingOrders().Wait();
            return "ok";

        }

        [HttpPost("dvf")]
        [EnableCors()]
        public async Task<string> dvf(CancellationToken cancellationToken)
        {
            await finder.Find(cancellationToken);
            return "ok";

        }

        [HttpPost("killd")]
        [EnableCors()]
        public async Task<string> killd(CancellationToken cancellationToken)
        {
            await killer.Kill(cancellationToken);
            return "ok";

        }
    }
}
