from Pedals.Distortion.distortionPedal import DistortionPedal
from Pedals.Delay.delayPedal import DelayPedal
from Pedals.LoFiModulator.lofiPedal import LoFiPedal
from Pedals.Overdrive.overdrivePedal import OverdrivePedal
from Pedals.PitchShift.pitchshiftPedal import PitchShiftPedal


def initializePedal(pedal_type: str, params: []):
    match pedal_type:
        case 'distortion':
            if len(params) > 4:
                raise IndexError(f"Too many input parameters ({len(params)}) for {pedal_type} pedal.")
            else:
                return DistortionPedal(params[0], params[1], params[2], params[3])
        case 'delay':
            if len(params) > 2:
                raise IndexError(f"Too many input parameters ({len(params)}) for {pedal_type} pedal.")
            else:
                return DelayPedal(params[0], params[1])
        case 'lofimodulator':
            if len(params) > 1:
                raise IndexError(f"Too many input parameters ({len(params)}) for {pedal_type} pedal.")
            else:
                return LoFiPedal(params[0])
        case 'overdrive':
            if len(params) > 4:
                raise IndexError(f"Too many input parameters ({len(params)}) for {pedal_type} pedal.")
            else:
                return OverdrivePedal(params[0], params[1], params[2], params[3])
        case 'pitchshift':
            if len(params) > 2:
                raise IndexError(f"Too many input parameters ({len(params)}) for {pedal_type} pedal.")
            else:
                return PitchShiftPedal(params[0], params[1])
        case None:
            raise NotImplementedError("Please enter a valid pedal name.")
        case _:
            raise NameError(f"'{pedal_type}' is not the name of a valid pedal.")
