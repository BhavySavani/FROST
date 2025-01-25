# FROST: Free and Real-Time Operating System Development Tool

## Abstract
Satellite development with the rapid advancement of space technology calls for innovative and efficient solutions. Traditional methods of configuring FPGA-based satellite systems are labor-intensive, requiring knowledge in FPGA configuration, Verilog coding, and bitstream generation. This creates bottlenecks, delays, increased costs, and barriers for those without technical expertise.

Our proposed software automates the FPGA configuration based on selected sensors and devices, generating Verilog files and bitstreams without any input from the user. This reduces the time and effort required for system configuration, freeing resources for other aspects of satellite development. The software is user-friendly, efficient, and adaptable, making it highly valuable for satellite and payload projects. By democratizing satellite design, it empowers developers of varied expertise levels to contribute to complex projects, fostering innovation and accelerating technological advancement.

## Introduction

### Background
Satellite design and configuration are complex processes, requiring significant manual intervention and specialized skills in FPGA configuration, Verilog coding, and bitstream generation. These traditional methods increase project costs and cause delays.

### Problem Statement
Configuring FPGAs for satellite systems is labor-intensive and requires specialized knowledge, creating bottlenecks in development. A solution is needed to automate these tasks, reduce reliance on expert knowledge, and cut down development time.

### Objective
The software aims to simplify and accelerate satellite system configuration by automating FPGA configuration based on selected sensors and devices, generating Verilog files and bitstreams with minimal manual input.

### Scope
Key features of the software include:
- Automatic FPGA configuration based on selected sensors/devices.
- Generation of Verilog files specific to chosen functions and communication protocols.
- Bitstream generation ready for deployment.
- A user-friendly interface requiring no coding expertise.

### Importance
This software revolutionizes satellite development workflows by saving time and reducing costs. It democratizes the design process, enabling contributors of varying expertise levels to participate in innovation and accelerate technological progress.

## Difference from Traditional HLS Software
Unlike traditional High-Level Synthesis (HLS) tools, our software is tailored for users without coding expertise. Key differentiators include:
- GUI-driven design for parameter selection instead of manual Verilog coding.
- Descriptive, intuitive terminology familiar to systems and hardware engineers.
- Guidance and prompts for configuration to ensure accessibility.

By abstracting complexities into user-friendly options, the software broadens the contributor base for satellite projects, enhancing innovation and collaboration.

## Software Overview

### 1. User Interface
Developed using PyQt 5, the GUI provides an intuitive setup process, requiring minimal user input.

### 2. FPGA Board Selection
Users specify the FPGA model, and constraints are set based on:
- **Manufacturer Constraints**: Predefined pin availability for I/O and other uses.
- **Hardware Engineer Constraints**: Optional grouping of pins by circuit and requirements.

### 3. Sensor/Device Selection
Users select sensors/devices, with communication protocols and clock frequencies automatically retrieved from the datasheets.

### 4. Verilog File Generation
Based on the chosen FPGA and sensors/devices, the software generates:
- **Core IP Verilog Files**: Specific to each sensor/device.
- **Frequency Scalers**: To match required sensor frequencies.
- **Top Module**: Integrating all IPs.

Additionally, a configuration file is generated with details of the FPGA, sensors/devices, and their configurations.

### 5. Bitstream Generation
The application produces a Python script to compile the configuration file and generate a bitstream, ready for FPGA deployment. Steps include:
- Generating a Python script for compilation.
- Creating a Verilog project bitstream.
- Instructions for FPGA bitstream upload.

## Technical Feasibility

### Technology Stack
- **Programming Language**: Python for backend development.
- **GUI Framework**: PyQt 5 for a user-friendly interface.
- **FPGA Tools**: Toolchains like Libero Design Suite for bitstream generation.
- **Data Storage**: JSON/SQLite for configuration files and user input.
- **Version Control**: Git for code management.

### Technical Challenges and Mitigation
1. **Integration with FPGA Tools**:
   - **Challenge**: Seamless integration for bitstream generation.
   - **Mitigation**: Utilize backend files from FPGA design software toolchains.

2. **Automating Verilog Generation**:
   - **Challenge**: Accurate Verilog file generation for various configurations.
   - **Mitigation**: Modular approach and comprehensive testing.

3. **User Interface Usability**:
   - **Challenge**: Ensuring a user-friendly interface for all experience levels.
   - **Mitigation**: Iterative design with user feedback.

## Conclusion
This project introduces innovative software to automate FPGA-based satellite system configuration. By simplifying critical tasks like Verilog file generation and bitstream creation, the software reduces dependency on expert knowledge and democratizes satellite development. The user-friendly, efficient tool empowers developers to contribute to complex projects, fostering innovation and accelerating space technology advancements.
