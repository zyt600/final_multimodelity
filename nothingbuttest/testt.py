import ffmpeg

aw = 0.7548823279761039
ah = 0.5885644375434604
out, _ = (ffmpeg
          .input("../data/videos/1W4s1_5GV4c.mp4", ss=91, t=3.3)
          .filter('fps', fps=10)

          .crop('(iw - {})*{}'.format(224, aw),
                '(ih - {})*{}'.format(224, ah),
                str(224), str(224))
          .hflip()
          .output('pipe:', format='rawvideo', pix_fmt='rgb24')
          .run(capture_stdout=True, quiet=True)
          )
print(type(out))
print(out)
print()
print(type(_))
print(_)
print("finish")
