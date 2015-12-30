import redis
import pywapi
import string

#vancouver = pywapi.get_weather_from_weather_com('CAXX0518')

#print "It is " + string.lower(vancouver['current_conditions']['text']) + " at " + string.lower(vancouver['current_conditions']['temperature']) + vancouver['units']['temperature'] + " with " + string.lower(vancouver['current_conditions']['humidity']) + "% humidity"

#print vancouver


r = redis.StrictRedis(host='localhost', port=6379, db=0)

pubsub = r.pubsub(ignore_subscribe_messages=True)

pubsub.subscribe('temperature')

temp = 4.356

while True:
	r.publish('temperature', temp + 1)
	time.sleep(1)



print pubsub.get_message()
print pubsub.get_message()











