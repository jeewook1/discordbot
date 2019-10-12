import discord
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print('ready')
    game =  discord.Game("파밍봇")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('/도움말'):
        await message.channel.send('안녕하세요 파밍봇입니다!\n파밍봇의 명령어는 다음과 같습니다.\n\n - 추가예정')

    if message.content.startswith('/사진'):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith('/뮤트'):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)
        await message.channel.send('뮤트 완료')

        if message.content.startswith('/뮤트해제'):
            author = message.guild.get_member(int(message.content[6:24]))
            role = discord.utils.get(message.guild.roles, name="뮤트")
            await author.remove_roles(role)
            await message.channel.send('뮤트해제 완료')

        if message.content.startswith('/경고'):
            author = message.guild.get_member(int(message.content[4:22]))
            file = openpyxl.load_workbook("경고.xlsx")
            sheet = file.active
            i = 1
            while True:
                if sheet["A" + str(i)].value == str(author.id):
                    sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                    file.save("경고.xlsx")
                    if sheet["B" + str(i)].value == 10:
                        await message.guild.ban(author)
                        await message.channel.send('경고를 총 10회 받았습니다. 서버에서 추방됩니다. ')
                    else:
                        await message.channel.send('경고를 1회 받았습니다.')
                    break
                if sheet["A" + str(i)].value == None:
                    sheet["A" + str(i)].value = str(author.id)
                    sheet["B" + str(i)].value = 1
                    file.save("경고.xlsx")
                    await message.channel.send('경고를 1회 받았습니다.')
                    break
                i += 1

client.run("NjMyNDQ1NTA2Nzg1NjQwNDQ4.XaHw4A.rbLqGJjlgqbk7OhWBhNYP_HAteo")