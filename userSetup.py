# --- {{{ZOMBIE INCLUDE START}}} ---
# The following code and the tags above/bellow are auto-generated through zombie pipeline. Do not change it or your changes could be deleted.

import maya.cmds as cmds

# -------------------------------------------------------------------------------------
def setup_zombie_port():
    """
    Create a command port for zombie pipeline tool
    """
    
    # Read port from file ... use default on problem
    # -------------------------------------------------------------------------------------
    config_file = "N:\\PSL_GLOBALS\\PSL_Pipeline\\src\\tools\\zombie\\zombie\\config\\maya_commandport.cfg"
    try:
        import zombie.config.maya as maya_conf
        port = maya_conf.port
        print ("PSL_PIPELINE: Port from zombie config used.")

    except:

        print ("PSL_PIPELINE: Using default port")
        port = "10101"

    
    # Try to open the port
    # -------------------------------------------------------------------------------------
    if cmds.commandPort(':%s' % str(port), q=True) !=1:
        try:
            cmds.commandPort(n=':%s' % str(port), eo = False, nr = False)
        except RuntimeError:
            print ("PSL_PIPELINE: CommandPort %s could not be opened. Possible that another maya instance occupies it?" % str(port))
        else:
            print ("PSL_PIPELINE: CommandPort %s opened" % str(port))
    else:
        print ("PSL_PIPELINE: CommandPort %s already opened" % str(port))

setup_zombie_port()

# --- {{{ZOMBIE INCLUDE END}}} ---
