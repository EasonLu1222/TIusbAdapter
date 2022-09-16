import clr                                          # Import clr from 'pythonnet' to interface runtime engine with .net
from System import Byte

class USB_TO_GPIO(object):

    def __init__(self):
        """ SAA adapter constructor -  discovering a device via the SMBus API.
            This library file provides you with the information required to use functions for remotely controlling your instrument.

            from usb-to-gpio import USB_TO_GPIO                                             # Importing USB_TO_GPIO file

            TI = USB_TO_GPIO()                                                              # Initialize & opens an instrument reference

            TI.configure(pec_enabled=False)                                                 # Selects 100-KHz/400-KHz bus speed & PEC mode
            TI.send_byte(dev_addr=0x001, cmd_addr=0x00)                                     # Performs a “Send_Byte”
            TI.write_byte(dev_addr=0x01, cmd_addr=0x00, data=0x00)                          # Performs a “Write_Byte”

            TI.close()                                                                      # Close the device reference

        """
        try:
            clr.AddReference("C:\\Program Files (x86)\\Texas Instruments\\Fusion Digital Power Studio\\bin\\TIDP.SAA.dll")    # Load the dll file(C:\\ folder)
            import TIDP.SAA as API                                                                              # Import TIDP.SAA dll file

            if API.SMBusAdapter.Discover() != 0:                                                                # Find an adapter
                self.device = API.SMBusAdapter.Adapter                                                          # Import class from C# namespace
                print('Device has opened')
            else:
                print("No Adapter Found")
        except:
            self.import_error()


    def __repr__(self):
        ''' print statement to compute the "informal" string representation of an object '''
        return repr(self.device)

    ###########################################
    # Error Handler
    ###########################################

    def import_error(self):
        ''' Update import error reported by the system of loading dll driver error.
        '''
        print("dll file not loaded, 'TI USB-TO-GPIO driver was not present/installed'.")
        exit()

    def exception_handler(self, exception):
        print("Exception occured:", exception)


if __name__ == "__main__":
    main = USB_TO_GPIO()

