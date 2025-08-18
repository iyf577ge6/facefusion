FaceFusion
==========

> Industry leading face manipulation platform.

[![Build Status](https://img.shields.io/github/actions/workflow/status/facefusion/facefusion/ci.yml.svg?branch=master)](https://github.com/facefusion/facefusion/actions?query=workflow:ci)
[![Coverage Status](https://img.shields.io/coveralls/facefusion/facefusion.svg)](https://coveralls.io/r/facefusion/facefusion)
![License](https://img.shields.io/badge/license-OpenRAIL--AS-green)

Preview
-------

![Preview](https://raw.githubusercontent.com/facefusion/facefusion/master/.github/preview.png?sanitize=true)

Installation
------------

The official [installation guide](https://docs.facefusion.io/installation) provides detailed information. A quick start on Linux/macOS:

```bash
git clone https://github.com/facefusion/facefusion.git
cd facefusion
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python facefusion.py run
```

Expose the web interface over the internet with [Ngrok](https://ngrok.com/):

```bash
pip install pyngrok
ngrok config add-authtoken <YOUR_NGROK_TOKEN>
ngrok http 7860
```

Kaggle Notebook
---------------

A starter notebook is included at [`notebooks/facefusion_kaggle.ipynb`](notebooks/facefusion_kaggle.ipynb). Use it in a Kaggle environment to install FaceFusion, open an Ngrok tunnel and run the application:

1. Upload the notebook to Kaggle or copy its cells into a new notebook.
2. Replace `YOUR_NGROK_TOKEN` with your token.
3. Run all cells and open the printed Ngrok URL to access the interface.

Custom Project Name
-------------------

To replace every occurrence of `facefusion` with a name of your choice, run:

```bash
python rename_project.py
```

The script prompts for a new name and updates text files throughout the repository.

Usage
-----

Run the command:

```
python facefusion.py [commands] [options]

options:
  -h, --help                                      show this help message and exit
  -v, --version                                   show program's version number and exit

commands:
    run                                           run the program
    headless-run                                  run the program in headless mode
    batch-run                                     run the program in batch mode
    force-download                                force automate downloads and exit
    benchmark                                     benchmark the program
    job-list                                      list jobs by status
    job-create                                    create a drafted job
    job-submit                                    submit a drafted job to become a queued job
    job-submit-all                                submit all drafted jobs to become a queued jobs
    job-delete                                    delete a drafted, queued, failed or completed job
    job-delete-all                                delete all drafted, queued, failed and completed jobs
    job-add-step                                  add a step to a drafted job
    job-remix-step                                remix a previous step from a drafted job
    job-insert-step                               insert a step to a drafted job
    job-remove-step                               remove a step from a drafted job
    job-run                                       run a queued job
    job-run-all                                   run all queued jobs
    job-retry                                     retry a failed job
    job-retry-all                                 retry all failed jobs
```

Documentation
-------------

Read the [documentation](https://docs.facefusion.io) for a deep dive.
