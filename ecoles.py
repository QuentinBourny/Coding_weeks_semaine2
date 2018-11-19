import matplotlib.pyplot as plt





Ecoles = {'CentraleSupelec' : 'gold',                   # Concours Centrale
          'Centrale Lyon' : 'orangered',
          'Centrale Nantes' : 'darkorange',
          'Centrale Lille' : 'peru',
          'Centrale Marseille' : 'orange',
          'Centrale Casablanca' : 'tomato',
          '''Institut d'Optique''' : 'lightsalmon',
          'ENSEA' : 'chocolate',
          'Ecole Navale' : 'maroon',
          'UTT' : 'firebrick',
          'Ponts ParisTech' : 'cyan',               # CCMP
          'ISAE Supaero' : 'darkturquoise',
          'ENSTA ParisTech' : 'steelblue',
          'Telecom' : 'mediumblue',
          'Mines ParisTech' : 'deepskyblue',
          'Mines Nancy' : 'cornflowerblue',
          'Mines Saint-Etienne' : 'navy',
          'IMT Atlantique' : 'royalblue',
          'ENSAE' : 'dodgerblue',
          'Chimie ParisTech' : 'mediumslateblue',
          'Polytechnique' : 'black',                    # X-ENS
          'ENS Ulm' : 'mediumseagreen',
          'ENS Lyon' : 'chartreuse',
          'ENS Paris Saclay' : 'mediumspringgreen',
          'ENS Rennes' : 'forestgreen'}

n = len(Ecoles)
print(n)

plt.clf()
compteur  = 1
for key in Ecoles :
    plt.plot( [key],[compteur], marker = 'o', color = Ecoles[key])
    compteur += 1

plt.show()

