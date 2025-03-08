from PIL import Image
import os

def split_gif(gif_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    gif = Image.open(gif_path)

    with Image.open(gif_path) as img:
        frame_number = 0

        while True:
            frame_filename = os.path.join(output_folder, f"frame_{frame_number:03d}.png")
            img.save(frame_filename)

            frame_number += 1

            try:
                img.seek(img.tell() + 1)
            except EOFError:
                break

def attach_gif(frames_folder, output_gif):
    if os.path.exists(frames_folder):
        images = os.listdir(frames_folder)
        images.sort()
        images = [os.path.join(frames_folder, image) for image in images]

        frames = [ Image.open(frame) for frame in images]
        frames[0].save(output_gif, save_all=True, append_images=frames[1:], loop= 0, duration=80, transparency = 1 )


if __name__ == "__main__":
    attach_gif("final_boykisser", "final.gif")
