import argparse
import traceback
from whisper_live.client import TranscriptionClient
import sounddevice as sd


def main_client(args):
    try:
        while True:
            transcription_client = TranscriptionClient(host=args.server, port=args.port,device_index=args.device_index)
            transcription_client()
    except Exception as e:
        traceback_info = traceback.format_exc()
        print(traceback_info)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p',
                        type=int,
                        default=9090,
                        help="Websocket port to run the server on.")
    parser.add_argument('--server', '-s',
                        type=str,
                        default='0.0.0.0',
                        help="Host for the server.")
    parser.add_argument('--device_index', '-dv',
                        type=int,
                        default=4,
                        help="Device index")
    args = parser.parse_args()
    s = sd.query_devices()
    for d in s:
        print(f"device={d}")
    main_client(args)




