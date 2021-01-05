import asyncio
import orm
from models import User, Blog, Comment
from aiomysql import create_pool

async def check():
	async with create_pool(host='localhost', port=3306,user='www-data', password='www-data',db='awesome', loop=loop) as pool:
		async with pool.acquire() as conn:
			async with conn.cursor() as cur:
				await cur.execute("SELECT count(*) from users;")
				value = await cur.fetchone()
				print('the number is :',value)
				
async def count():
	await orm.create_pool(loop,	user='www-data', password='www-data',db='awesome')
	result = await orm.select('select * from users','')
	print('the number of result is :',len(result))


async def drop():
	await orm.create_pool(loop,	user='www-data', password='www-data',db='awesome')
	result = await orm.execute('delete from users where name regexp ?','^a')
	print('the number of afftecd row is :',result)

	
async def add():
    await orm.create_pool(loop,
    	user='www-data', password='www-data', 
    	db='awesome')
    u = User(name='apple', email='apple@example.com', passwd='15335179426', image='about:blank')
    await u.save()
    


#if __name__ == '__main__':
#    loop = asyncio.get_event_loop()
#    loop.run_until_complete(test(loop))
#    loop.close()

#xloop.run_until_complete(test())

loop = asyncio.get_event_loop()
loop.run_until_complete(check())
loop.run_until_complete(count())
loop.run_until_complete(add())
loop.run_until_complete(count())
loop.run_until_complete(drop())
loop.run_until_complete(count())

for x in check():
	pass
	
#loop.close()


#参考来源：https://aodabo.tech/blog/001546713871394a2814d2c180b4e6f8d30c62a3eaf218a000 大卜