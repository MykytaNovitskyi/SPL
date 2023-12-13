from __future__ import division
from colorama import Fore
from Lab5.cube import CubeDrawer

def main():
    try:
        x_size = int(input("Enter the cube size along the x-axis: "))
        y_size = int(input("Enter the cube size along the y-axis: "))
        z_size = int(input("Enter the cube size along the z-axis: "))
    except ValueError:
        print("Invalid input format. Using default sizes (1, 1, 1).")
        x_size, y_size, z_size = 1, 1, 1

    selected_color = input("Enter the color code (e.g., RED, GREEN, BLUE): ")

    try:
        color_code = getattr(Fore, selected_color.upper())
    except AttributeError:
        print("Invalid color code. Using white color by default.")
        color_code = Fore.WHITE

    cube_drawer = CubeDrawer(x_size, y_size, z_size, color_code)
    cube_str = cube_drawer.draw_cube()
    print(cube_str)

    save_cube = input("Do you want to save the cube to a file? (Yes/No): ").lower()
    if save_cube == "yes":
        cube_drawer.save_to_file(cube_str)

    generate_square = input("Do you want to generate a square? (Yes/No): ").lower()

    if generate_square == "yes":
        square_str = cube_drawer.draw_square(y_size)
        print(square_str)

        save_square = input("Do you want to save the square to a file? (Yes/No): ").lower()
        if save_square == "yes":
            cube_drawer.save_to_file(square_str)

if __name__ == "__main__":
    main()
