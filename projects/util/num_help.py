''' Helper functions for number limits'''

def clamp(value, minn, maxn):
    ''' restrict the range a number can have'''
    return max(min(maxn, value), minn)
