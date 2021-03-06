[![DOI](https://zenodo.org/badge/442127073.svg)](https://zenodo.org/badge/latestdoi/442127073)

# jedi-datasets

This repository contains the experimental data for JSON similarity lookups that are published in the following publication:

```
@inproceedings{huetter2021jedi,
  title        = {{JEDI}: These aren't the {JSON} documents you're looking for...},
  author       = {H{\"u}tter, Thomas and Augsten, Nikolaus and Christoph M, Kirsch and Michael J, Carey and Li, Chen},
  year         = 2022,
  booktitle    = {Proceedings of the 2022 International Conference on Management of Data}
}
```

## Fetch, preprocess, and analyze data

The raw JSON datasets are fetched from repositories (see directory `raw-data`) and converted into bracket notation which serves as the input data for the algorithms (see directory `input-data`). Further, the characteristics of the JSON datasets are analyzed. All steps are performed by the following script:
```
sh scripts/download-prepare.sh
```

This process takes approximately one hour for all datasets. One might 
consider to exclude datasets that are not needed.

## Datasets

The following datasets are included:
- arxiv
- cards
- clothing
- dblp
- denf
- device
- face
- fenf
- movies
- nasa
- nba
- reads
- recipes
- reddit
- schema
- smsen
- smszh
- spotify
- standev
- stantrain
- trees
- twitter
- twitter2
- virus
