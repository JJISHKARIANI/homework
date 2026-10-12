def greeter_bot():
      name = yield "enter your name"
      
      
      while True:
          name = yield f"hello {name}"




bot= greeter_bot()     
print(next(bot))   
print(bot.send("Jaba"))