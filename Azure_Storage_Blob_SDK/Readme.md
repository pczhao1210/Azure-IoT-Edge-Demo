## Azure Storage Blob SDK for Edge Blob Module Arm64v8-preview

# This SDK is based on Azure Storage Blob SDK version 2.1, please use this [Link](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python-legacy) to find the usage.

To use this wheel, please first update your pip to latest version.

To install this module:
```
  python -m pip install --upgrade pip
  pip uninstall azure_storage_blob
  pip install azure_storage_blob-2.1.0-py2.py3-none-any.whl
```

To test this module properly installed:
```
  python
  from azure.storage.blob import __version__
  print(__version__)
```

The version should be:
```
  2.1.0 for IoT Edge Blob Module Arm64v8
```

Disclaimer:
Please use this SDK and script only for experiment situation.
