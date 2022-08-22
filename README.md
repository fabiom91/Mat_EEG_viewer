# MATlab EEG reader
Simple `.mat` EEG reader made in `python` using `mne`: https://mne.tools/stable/index.html

## Windows
open a `shell` in this folder then run: `run_windows <EEG_FILENAME>` where `<EEG_FILENAME>` is the name of the EEG file to analyse.

## Mac and Linux
open a `terminal` in this folder then run `./run_unix.sh <EEG_FILENAME>` where `<EEG_FILENAME>` is the name of the EEG file to analyse.
> Note: if you get an error, you might have to give `run_unix.sh` permission to execute code. You can do so by running `sudo chmod u+x run_unix.sh`

---

The EEG files should be stored in the `EEG_Folder` of this repo. You can change this default behaviour by creating a `JSON` file called `secrets.json` in the main directory:
```json
{
    "EEG_folder": "<PATH_TO_MY_FOLDER>"
}
```