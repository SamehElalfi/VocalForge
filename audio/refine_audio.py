from .voice_detection import VoiceDetection
from .overlap import Overlap
from .isolate import IsolateSpeaker
from .export_audio import ExportAudio

class RefineAudio():
    def __init__(
        self,
        input_dir=None,
        vad_dir=None,
        overlap_dir=None,
        sample_dir=None,
        verification_dir=None,
        isolated_dir=None,
        noise_removed_dir=None,
        normalization_dir=None,
        export_dir=None,
        sample_rate=None,
        vad_theshold=None,
        noise_aggressiveness=None,
        verification_threshold=None,
        speaker_id=None,
    ):
        self.Input_Dir = input_dir
        self.VAD_dir = vad_dir
        self.Overlap_Dir = overlap_dir
        self.Sample_Dir = sample_dir
        self.Verification_Dir = verification_dir
        self.Isolated_Dir = isolated_dir
        self.Export_Audio_Dir = export_dir
        self.VAD_Threshold = vad_theshold
        self.Noise_Aggressiveness = noise_aggressiveness
        self.Verification_Threshold = verification_threshold
        self.Speaker_Id = speaker_id
        self.Noise_Removed_Dir = noise_removed_dir
        self.Normalized_Dir = normalization_dir
        self.Sample_Rate = sample_rate

        self.VoiceDetection = VoiceDetection(
            vad_threshold=self.VAD_Threshold, 
            noise_aggressiveness=self.Noise_Aggressiveness,
            input_dir=self.Input_Dir,
            output_dir=self.VAD_dir,
            sample_dir=self.Sample_Dir,
        )
        self.Overlap_Remover = Overlap(
            input_dir=self.VAD_dir,
            output_dir=self.Overlap_Dir,
        )
        self.Isolate_Speaker = IsolateSpeaker(
            input_dir=self.Overlap_Dir,
            verification_dir=self.Verification_Dir,
            isolated_speaker_dir=self.Isolated_Dir,
            verification_threshold=self.Verification_Threshold,
            speaker_id=self.Speaker_Id,
        )
        self.Export_Audio = ExportAudio(
            input_dir=self.Isolated_Dir,
            export_dir=self.Export_Audio_Dir,
            noise_removed_dir=self.Noise_Removed_Dir,
            normalization_dir=self.Normalized_Dir,
            sample_rate=self.Sample_Rate,
        )
    
    def run_all(self):
        self.VoiceDetection.run_vad()
        self.Overlap_Remover.run_overlap()
        self.Isolate_Speaker.run_seperate_speakers()
        self.Isolate_Speaker.run_verify()
        self.Export_Audio.run_export()