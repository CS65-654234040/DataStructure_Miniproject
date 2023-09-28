# Visualization function with steps
def visualize_merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        visualize_merge_sort(arr, start, mid)
        visualize_merge_sort(arr, mid + 1, end)

        left_half = arr[start:mid + 1]
        right_half = arr[mid + 1:end + 1]

        i = j = 0
        k = start

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        # Display the current state of the array and wait for user interaction
        canvas.delete("rectangles")
        draw_rectangles(arr)
        root.update()
        root.after(1000)  # Wait for 1 second

# Add a label to display the current step
step_label = tk.Label(root, text="Current Step: 0")
step_label.pack()

# Global variable to keep track of the step
current_step = 0

# Update the step label
def update_step_label():
    global current_step
    current_step += 1
    step_label.config(text=f"Current Step: {current_step}")

# Visualization function for merge step
def visualize_merge_step(arr, start, mid, end):
    left_half = arr[start:mid + 1]
    right_half = arr[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    # Display the current state of the array and wait for user interaction
    canvas.delete("rectangles")
    draw_rectangles(arr)
    root.update()
    update_step_label()
    root.after(1000)  # Wait for 1 second

# Modify the existing visualize_merge_sort function
def visualize_merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        visualize_merge_sort(arr, start, mid)
        visualize_merge_sort(arr, mid + 1, end)
        visualize_merge_step(arr, start, mid, end)

# Reset the step count
def reset_step_count():
    global current_step
    current_step = 0
    step_label.config(text="Current Step: 0")

# Create a button to start sorting and reset step count
sort_button = tk.Button(root, text="Start Merge Sort", command=lambda: [reset_step_count(), start_merge_sort()])
sort_button.pack()

# Run the main loop
root.mainloop()
