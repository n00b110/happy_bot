from moviepy.editor import VideoFileClip

def convert_to_black_and_white(input_file, output_file):
    clip = VideoFileClip(input_file)
    bw_clip = clip.fx(vfx.blackwhite)
    bw_clip.write(output_file, codec='libx264', audio_codec='aac')
