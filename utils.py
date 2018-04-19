import time

def measure_call(target, name):
    start = time.clock()
    try:
        target()
        elasped = time.clock() - start
        print('%s: %g ms' % (name, elasped * 1000))
    except RuntimeError as e:
        print('%s: %s' % (name, e))
        
def fibonacci_top_down_print_stack(n):
    def print_stack(message, depth):
        result.append(f'{"-" * depth}{message}')

    def fibonacci_top_down_detail(n, memo={}, depth=0):
        # check if solution already exists
        if n in memo:
            return memo[n]

        if n == 1:
            print_stack(f'F1 = 0 (base case)', depth)
            memo[n] = 0
        elif n == 2:
            print_stack(f'F2 = 1 (base case)', depth)
            memo[n] = 1
        else:
            memo[n] = fibonacci_top_down_detail(n - 1, memo, depth + 1) + fibonacci_top_down_detail(n - 2, memo, depth + 1)
            print_stack(f'F{n} = F{n-1} + F{n-2}', depth)

        return memo[n]

    result = []
    value = fibonacci_top_down_detail(n)
    print('\n'.join(result))
    return value

def fibonacci_buttom_up_print_dp(n):
    result = []
    
    def print_dp(dp, n):
        result.append((' ' if n < 10 else '') + f'F{n}: [' + ','.join('%2s' % (x if x is not None else '•') for x in dp) + ']')
    
    def fibonacci_buttom_up_detail(n):
        if n==1:
            return 0
        if n==2:
            return 1

        dp = [None] * (n + 1)
        dp[1] = 0
        dp[2] = 1

        k = 3
        while k <= n:
            dp[k] = dp[k - 1] + dp[k - 2]
            print_dp(dp, k)
            k += 1

        return dp[n]
    
    value = fibonacci_buttom_up_detail(n)
    print('\n'.join(result))
    return value