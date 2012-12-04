#!/usr/bin/python

import os
from optparse import OptionParser

class NodeRoles:
    
    def get_opts(self):
        desc = """simple program for doing trimming the time series"""
        self.usage = "usage: %prog [options]"
        self.parser = OptionParser(description=desc, version="%prog Dec.2012")
        self.parser.add_option("--subject", dest="subject",
                               help="specify the subject")
        self.parser.add_option("--condition", dest="condition",
                               help="specify the condition")

        (self.options, args) = self.parser.parse_args()


    def find_role(self):
        """
        Read in the participation coefficient and modular degree files
        Then map them from string to floating point values
        """
        par = open(self.options.subject+"."+self.options.condition+".part_coef","r").readlines()
        deg = open(self.options.subject+"."+self.options.condition+".mod_degree","r").readlines()
        par = map(float, map(lambda par: par.strip(), par))
        deg = map(float, map(lambda deg: deg.strip(), deg))

        role = []
        """
        roles, value ranges follow Guimera & Amaral, 2005
        """
        for val in range(len(par)):
            if deg[val] < 2.5:
                if par[val] <= .05:
                    role.append(1)
                elif par[val] > .05 and par[val] <= .62:
                    role.append(2)
                elif par[val] > .62 and par[val] <= .80:
                    role.append(3)
                elif par[val] > .80:
                    role.append(4)
            elif deg[val] >= 2.5:
                if par[val] <= .30:
                    role.append(5)
                elif par[val] > .3 and par[val] <= .75:
                    role.append(6)
                elif par[val] > .75:
                    role.append(7)

        rolesout = ""
        for i in role:
            rolesout += str(i)+"\n"

        outf = open(self.options.subject+"."+self.options.condition+".node_roles","w")
        outf.write(rolesout)
        outf.close()
        return rolesout


def main():
    NR = NodeRoles()
    NR.get_opts()
    os.chdir(os.environ["state"]+"/"+NR.options.subject+"/corrTRIM_BLUR/")
    print os.getcwd()
    NR.find_role()
    
if __name__ == "__main__":
    main()
