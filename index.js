const Discord = require('discord.js');
const client = new Discord.Client();
const token = 'NzQ2NzE0NjMzMzAxMzkzNDQ4.X0EWMQ.ffgNAooSLs-56mxTLqx8SCHmCQK';

client.on('ready', () => {
  console.log('켰다.');
});

client.on('message', (message) => {
  if(message.content === 'ping') {
    message.reply('pong');
  }
});

client.login(token);