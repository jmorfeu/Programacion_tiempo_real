// See https://aka.ms/new-console-template for more information

using StackExchange.Redis;

class Program{
    static void Main(string[] args){
        
        var redisConnection = ConnectionMultiplexer.Connect("localhost");
        var subscriber=redisConnection.GetSubscriber();
        string channel = "eventos";

        subscriber.Subscribe(channel,(RedisChannel, value)=>
        { 
            Console.WriteLine(value);
        });
        Console.ReadLine();
    }
}