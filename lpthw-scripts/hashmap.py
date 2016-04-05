def new(num_buckets=256):
    # initialises aMap with the given number of buckets
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    # given a key, create number, convert it to index for aMap's buckets
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    # given a key, find the bucket where it goes
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    # returns the index, key, value of a slot found in a bucket
    # returns -1 key and default (None if not set) when not found
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v

    return -1, key, default

def get(aMap, key, default=None):
    # gets value for the given bucket or default
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    # sets key to the value replacing any existing key
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not, create and append
        bucket.append((key, value))

def delete(aMap, key):
    # delete key for the given map
    bucket = get_bucket(aMap, key)

    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    # prints out the map
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print(k, v)
