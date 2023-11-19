from .environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_path = ''
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_path = ''
    settings.network_path = '/mnt/data/src/hockeymom_2/models/MixFormer/lib/test/networks/'    # Where tracking networks are stored.
    settings.nfs_path = ''
    settings.otb_path = ''
    settings.result_plot_path = '/mnt/data/src/hockeymom_2/models/MixFormer/lib/test/result_plots/'
    settings.results_path = '/mnt/data/src/hockeymom_2/models/MixFormer/lib/test/tracking_results/'    # Where to store tracking results
    settings.segmentation_path = '/mnt/data/src/hockeymom_2/models/MixFormer/lib/test/segmentation_results/'
    settings.tn_packed_results_path = ''
    settings.tpl_path = ''
    settings.trackingnet_path = ''
    settings.uav_path = ''
    settings.vot_path = ''
    settings.youtubevos_dir = ''

    settings.workspace_dir = "."  # Base directory for saving network checkpoints.
    settings.proj_dir = settings.workspace_dir

    settings.dataset_dir = f"{os.path.join(os.environ['HOME'], 'src', 'datasets')}"
    settings.tensorboard_dir = (
        settings.workspace_dir + "/tensorboard/"
    )  # Directory for tensorboard files.
    settings.pretrained_networks = settings.workspace_dir + "/pretrained_networks/"
    settings.sportsmot_dir = f"{settings.dataset_dir}/SportsMOT"
    settings.sportsmot_anno_dir = f"{settings.dataset_dir}/SportsMOT/tracking_annos"
    settings.mot17_dir = f"{settings.dataset_dir}/MOT17"
    settings.mot17_anno_dir = f"{settings.dataset_dir}/MOT17/tracking_annos"
    settings.mot20_dir = ""
    settings.mot20_anno_dir = ""
    settings.dancetrack_dir = f"{settings.dataset_dir}/DanceTrack"
    settings.dancetrack_anno_dir = f"{settings.dataset_dir}/DanceTrack/tracking_annos"
    settings.soccernet_dir = f"{settings.dataset_dir}/SoccerNet"
    settings.soccernet_anno_dir = f"{settings.dataset_dir}/SoccerNet/tracking_annos"
    settings.hockey_dir = f"{settings.dataset_dir}/hockeyTraining"
    settings.hockey_anno_dir = f"{settings.dataset_dir}/hockeyTraining/tracking_annos"
    settings.hockey_ch_ht_dir = f"{settings.dataset_dir}/hockeyTraining"
    settings.hockey_ch_ht_anno_dir = f"{settings.dataset_dir}/hockeyTraining/tracking_annos"
    settings.lasot_dir = ""
    settings.tnl2k_dir = ""
    settings.got10k_dir = ""
    settings.trackingnet_dir = ""
    settings.coco_dir = ""
    settings.lvis_dir = ""
    settings.sbd_dir = ""
    settings.imagenet_dir = ""
    settings.imagenetdet_dir = ""
    settings.ecssd_dir = ""
    settings.hkuis_dir = ""
    settings.msra10k_dir = ""
    settings.davis_dir = ""
    settings.youtubevos_dir = ""

    return settings

