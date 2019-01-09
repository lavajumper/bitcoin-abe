from .ScryptSxcAuxPowChain import ScryptSxcAuxPowChain

class Sexcoin(ScryptSxcAuxPowChain):
    def __init__(chain, **kwargs):
        chain.name='Sexcoin'
        chain.code3='SXC'
        chain.address_version = '\x3e'
        chain.script_addr_vers = '\x69'
        chain.magic = '\xfa\xce\x69\x69'
        ScryptSxcAuxPowChain.__init__(chain,**kwargs)
        
    datadir_conf_file_name = 'sexcoin.conf'
    datadir_rpcport = 9561
    datadir_p2port = 9560
