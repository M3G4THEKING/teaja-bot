from config import bot

@bot.command(name='source')
async def source(ctx):
    await ctx.send('I was created by dredgen_teaja. You can see the code that makes me work at https://github.com/thomas-j-sell/teaja-bot')


@bot.command(name='blurg')
async def blurg(ctx):
    await ctx.send('blurg')


@bot.command(name='thicc')
async def thicc(ctx):
    await ctx.send("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu")
