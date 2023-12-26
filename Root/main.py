from board import Pedalboard
from pedal import initializePedal
from audiofile import AudioFile




def printLogo():
    print('    ____           __      ____                         __                   ')
    print('   / __ \___  ____/ /___ _/ / /_  ____  ____ __________/ /       ____  __  __')
    print('  / /_/ / _ \/ __  / __ `/ / __ \/ __ \/ __ `/ ___/ __  /       / __ \/ / / /')
    print(' / ____/  __/ /_/ / /_/ / / /_/ / /_/ / /_/ / /  / /_/ /       / /_/ / /_/ / ')
    print('/_/    \___/\__,_/\__,_/_/_.___/\____/\__,_/_/   \__,_/  ( )  / .___/\__, /  ')
    print('                                                             /_/    /____/   ')
    print('\n\n\n')


def helpMenu():
    print("\n\nCommand Options:\n\tdisplay - prints all pedals currently on pedalboard"
          "\n\taddpedal - adds a pedal to the pedalboard"
          "\n\tdelpedal - deletes a pedal from the pedalboard"
          "\n\tinputfile - specifies mp3 input file path"
          "\n\tprocessfile - perform pedal operations on input file and output to specified path")

    print("\n\n\nCommand Input Arguments:\n\tdisplay - none"
          "\n\taddpedal - pedal type, pedal parameters, index(optional)"
          "\n\tdelpedal - pedal index on pedalboard"
          "\n\tinputfile - file path to .mp3 input file"
          "\n\tprocessfile - path to export processed .mp3 file to")

    print("\n\n\nCommand Examples:\n\t'display'"
          "\n\t'addpedal distortion [20, 3.7, 0.5, 1] 0'"
          "\n\t'delpedal 0'"
          "\n\t'inputfile C:\\Users\\Username\\Desktop\\guitar_part.mp3'"
          "\n\t'processfile C:\\Users\\Username\\Desktop\\processed_guitar_part.mp3'")

    print("\n\n\nPedal Parameters:"
          "\n\tdistortion pedal:"
          "\n\t\tdistortion: [min=0.0, max=1.0] - float indicating how much to distort audio signal"
          "\n\t\tcutoff: [min=0, max=int(+inf) - cutoff frequency for toning lowpass filter"
          "\n\t\tdepth: [min=0.0, max=1.0] - steepness of toning lowpass filter"
          "\n\t\tlevel: [min=0.0, max=1.0] - decibel boost after effects were applied to input signal"
          ""
          "\n\n\toverdrive pedal:"
          "\n\t\toverdrive: [min=0.0, max=1.0] - float indicating how much to overdrive audio signal"
          "\n\t\tcutoff: [min=0, max=int(+inf) - cutoff frequency for toning lowpass filter"
          "\n\t\tdepth: [min=0.0, max=1.0] - steepness of toning lowpass filter"
          "\n\t\tboost: [min=0.0, max=1.0] - decibel boost after effects were applied to input signal"
          ""
          "\n\n\tdelay pedal:"
          "\n\t\ttime: [min=0.0, max=1.0] - length of segments to copy and echo over audio signal"
          "\n\t\tdecay: [min=0.0, max=0.99] - rate of echo fading"
          ""
          "\n\n\tlofimodulator pedal:"
          "\n\t\tmodulation: [min=0.0, max=0.99] - how much compression/decompression should be applied to signal"
          ""
          "\n\n\tpitchshift pedal:"
          "\n\t\toctaves: [min=-3, max=3] - octave shift to apply to signal"
          "\n\t\tsemitones: [min=-11, max=11] - semitone shift to apply to signal"
          )


def mainLoop():

    pedalboard = Pedalboard()
    audio_file = AudioFile()
    printLogo()
    command, args, params = None, None, None

    while command != 'exit':

        command = input("Enter a command. Enter 'help' for a list of available commands. "
                        "Enter 'exit' to quit.")
        command, args = command.split(' ', maxsplit=1)
        command = command.lower()

        if command == 'help':
            helpMenu()
        elif command == 'exit':
            print("Goodbye.")
            break
        elif command == 'display':
            pedalboard.displayPedals()
        elif args is None:
            raise ValueError(f"Additional input needed for command '{command}'. Refer to"
                             f"'help' for more info.")
        elif command == 'addpedal':
            pedal_type, params = args.split(' ', maxsplit=1)
            params, index = params.rsplit(' ', maxsplit=1)
            pedal = initializePedal(pedal_type, eval(params))
            try:
                index = int(index)
            except ValueError:
                pedalboard.addPedal(pedal)
            else:
                pedalboard.addPedal(pedal_type, index=index)

        elif command == 'delpedal':
            index, extra = args.split(' ', maxsplit=1)
            if extra is not None:
                raise BufferError(f"Too many arguments for command 'delpedal'.")
            pedalboard.delPedal(int(index))

        elif command == 'inputfile':
            file, extra = args.split(' ', maxsplit=1)
            if extra is not None:
                raise BufferError(f"Too many arguments for command 'inputfile'.")
            audio_file.loadFile(file)

        elif command == 'processfile':
            out_file, extra = args.split(' ', maxsplit=1)
            if extra is not None:
                raise BufferError(f"Too many arguments for command 'processfile'.")
            pedalboard.processFile(audio_file, out_file)
        else:
            raise ValueError(f"Invalid input. Try again or consult 'help' for a list of valid commands.")


if __name__ == '__main__':
    mainLoop()


