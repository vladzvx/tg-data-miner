﻿using Common;
using Common.Models;
using DataFair.Services;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DataFair.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class CommandController
    {
        private readonly OrdersGenerator ordersGenerator;
        public CommandController(OrdersGenerator ordersGenerator)
        {
            this.ordersGenerator = ordersGenerator;
        }

        [HttpPost("GetFullChannel")]
        [EnableCors()]
        public string PostRequest()
        {
            ordersGenerator.CreateGetFullChannelOrders(800).Wait();
            return "ok";
            
        }

        [HttpPost("GetGroupsHistory")]
        [EnableCors()]
        public string PostRequest2()
        {
            ordersGenerator.CreateGroupHistoryLoadingOrders().Wait();
            return "ok";

        }
    }
}
