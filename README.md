# rqx-release-sw
Public released software for ROScube-X series.

Please go to [release page](https://github.com/Adlink-ROS/rqx-release-sw/releases) to download.

## FPGA Flash Tool

Currently, this tool only supports RQX-590 with ADLINK GMSL/FPDL board.

- fpga_flash_tool_0.9.0

## RQX590 FPGA Firmware

### How to get version
```bash
i2cget -f -y 2 0x66 0x01
```

The latest firmware:

- rqx590_0x24.vme


### How to flash

Please follow the instructions below to flash RQX590 FPGA:

1. Download and extract `rqx590_<ver>.vme.tgz` and `fpga_flash_tool_<ver>.tgz`

    ```bash
    tar zxvf fpga_flash_tool_0.9.0.tgz
    tar zxvf rqx590_0x24.vme.tgz
    cp rqx590_0x24.vme ./fpga_flash_tool_0.9.0/
    ```

2. Follow below commands to flash the FPGA:

    ```bash
    cd fpga_flash_tool_0.9.0
    chmod +x RQX590-JTAG.run
    sudo ./RQX590-JTAG.run -c rqx590_0x24.vme
    ```

    ![](pictures/fpga_flashing.png)

3. Read the FPGA register 0x01, you will get the FPGA firmware version if flashed successfully.

    ```bash
    i2cget -f -y 2 0x66 0x01
    ```
    ![](pictures/fpga_fw_0x24.png)

    Note: If FPGA failed to flash, please make sure the DIP switches on the IO Board are turned on.
    
    ![](pictures/fpga_dip_sw.png)