import subprocess


def download(video_id):
    try:
        subprocess.run(['youtube-dl', '-x', '--audio-quality', '0', '--audio-format', 'flac', '-o', '%(id)s.%(ext)s',
                        'https://youtube.com/watch?v=' + video_id])
    except AttributeError:
        subprocess.call(['youtube-dl', '-x', '--audio-quality', '0', '--audio-format', 'flac', '-o', '%(id)s.%(ext)s',
                        'https://youtube.com/watch?v=' + video_id])
