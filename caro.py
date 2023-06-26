import cairo

def generate_floor_plan(width, length, room_dimensions):
    surface = cairo.SVGSurface("floor_plan.svg", width, length)
    context = cairo.Context(surface)

    # Draw floor outline
    context.rectangle(0, 0, width, length)
    context.set_source_rgb(0.5, 0.5, 0.5)  # Set floor color
    context.fill()

    # Draw rooms
    for room in room_dimensions:
        room_width, room_length = room
        # Calculate room position based on dimensions
        room_x = (width - room_width) / 2
        room_y = (length - room_length) / 2

        context.rectangle(room_x, room_y, room_width, room_length)
        context.set_source_rgb(1, 1, 1)  # Set room color
        context.fill()

    surface.finish()
    print("Floor plan generated.")

# Example usage
width = 800
length = 600
room_dimensions = [(200, 300), (150, 250), (100, 200)]  # Example room dimensions

generate_floor_plan(width, length, room_dimensions)
