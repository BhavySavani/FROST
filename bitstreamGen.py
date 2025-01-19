from fpga.project import Project
import logging
prj = Project("vivado")
prj.set_part('xc7k160t-3-fbg484')
prj.add_files('uart/uart.v')
prj.add_files('uart/transmitter.v')
prj.add_files('uart/receiver.v')
prj.add_files('uart/baud_rate_gen.v')
prj.set_top('top_module.v')
try:
    prj.generate()
except Exception as e:
    logging.warning('{} ({})'.format(type(e).__name__, e))