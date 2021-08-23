buttons = [input().lower() for _ in range(int(input()))]
is_pink_button = lambda button: "pink" in button or "rose" in button
pink_button_count = len(list(filter(is_pink_button, buttons)))

if pink_button_count:
    print(pink_button_count)
else:
    print("I must watch Star Wars with my daughter")