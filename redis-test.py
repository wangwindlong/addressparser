import redis

r = redis.Redis(host='127.0.0.1', port=6379, password='N2vip_net', db=0, decode_responses=True)
test = r.get('test')
print("test={}".format(test))
if not test:
    r.set("test", "这个是测试")
test = r.get('test')
print("test={}".format(test))