import redis

def publicar_evento(evento):
    # Implementación para publicar eventos a Redis
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.publish('eventos', evento)