# MATSim Data Adapter: matsimDataAdapter (Python)
[![matsimDataAdapter Homepage](https://img.shields.io/badge/matsimDataAdapter-develop-orange.svg)](https://github.com/davidvelascogarcia/matsimDataAdapter/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/matsimDataAdapter.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/matsimDataAdapter/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/matsimDataAdapter.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/matsimDataAdapter)

- [MATSim Data Adapter: matsimDataAdapter (Python)](#matsim-data-adapter-matsimdataadapter-python)
  - [Introduction](#introduction)
  - [Running Software](#running-software)
    - [Arguments](#arguments)
  - [Requirements](#requirements)
  - [Status](#status)
  - [Related projects](#related-projects)

## Introduction

`matsimDataAdapter` is a module in `python` language that automate MATSim simulation database adapter generation.

Documentation available on [docs](https://davidvelascogarcia.github.io/matsimDataAdapter)

## Running Software

1. Run [matsimDataAdapter.py](./programs).

```bash
python3 matsimDataAdapter.py
```

### Arguments

Avaliable arguments allowed:

| Argument | Full  | Simple | Description  |
| -------  |  ---  |  ----  | -----------  |
|  Database  |  --database  |  -d  | Input source database  |
|  Input  |  --input  |  -i  | Input network image  |
|  Output  |  --output  |  -o  | Output adapted database  |

## Requirements

`matsimConfigGenerator` requires:

[Install pip3](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)

```bash
pip3 install -r requirements.txt
```

Tested on: `windows 10`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `kubuntu 20.04`.

## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/matsimDataAdapter.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/matsimDataAdapter)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/matsimDataAdapter.svg?label=Issues)](https://github.com/davidvelascogarcia/matsimDataAdapter/issues)

## Related projects

* [davidvelascogarcia: matsimConfigGenerator (Python)](https://github.com/davidvelascogarcia/matsimConfigGenerator)
* [davidvelascogarcia: matsimDataAdapter (Python)](https://github.com/davidvelascogarcia/matsimDataAdapter)
* [davidvelascogarcia: matsimDataGenerator (Python)](https://github.com/davidvelascogarcia/matsimDataGenerator)
* [davidvelascogarcia: matsimNetGenerator (Python)](https://github.com/davidvelascogarcia/matsimNetGenerator)
* [davidvelascogarcia: matsimPlansGenerator (Python)](https://github.com/davidvelascogarcia/matsimPlansGenerator)
* [davidvelascogarcia: matsimVoronoiGenerator (Python)](https://github.com/davidvelascogarcia/matsimVoronoiGenerator)
