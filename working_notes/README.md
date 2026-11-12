# troyraen/open-data-registry

[troyraen/open-data-registry](https://github.com/troyraen/open-data-registry) forked from [awslabs/open-data-registry](https://github.com/awslabs/open-data-registry)

## ODR process

[Onboarding Handbook](https://assets.opendata.aws/aws-onboarding-handbook-for-data-providers-en-US.pdf)

- [ ] Submit an application https://application.opendata.aws/.
    - See [templates/application.yaml](templates/application.yaml) for an IRSA starter-template.
    - Generally, this should be submitted and approved before proceeding.
      For NASA Space Act datasets, this can be done after submitting the PR.
- [ ] Submit a pull request to https://github.com/awslabs/open-data-registry/ with a yaml file containing the dataset metadata. More info can be found in the repo's README.
    - See [../README.md](../README.md) for AWS's instructions.
    - See [templates/metadata.yaml](templates/metadata.yaml) for a starter template.
    - See below to create a bare-bones html page that can be used for visual inspection (optional).
- [ ] Email [IRSA logo](/working_notes/IRSA_Logo_color_170.png) to opendata@amazon.com.

## Create files

```sh
dataset_name='FILL-IN'

# Start a new dataset yaml.
cp working_notes/templates/metadata.yaml datasets/${dataset_name}.yaml

# Edit the new yaml.

# Render as bare-bones html.
python working_notes/render_html.py $dataset_name
```

The current page is [https://registry.opendata.aws/spherex-qr/]. I made drafts of two versions updated with QR2 info and posted bare-bones rendered pages on my port:

* [spherex-qr-long|https://irsadev.ipac.caltech.edu:9051/cloud_access/odr-spherex-qr-long.html] lists all data products for both QRs separately, closely following the current page.
* [spherex-qr-short|https://irsadev.ipac.caltech.edu:9051/cloud_access/odr-spherex-qr-short.html] only lists QR1 and QR2 and points to the User Guide for info about the data products and directory structure.

The main "Description" (left-hand side) for each version is slightly different. Both versions have the same updates to "How to Cite".

[~desai] what do you want to see here?
