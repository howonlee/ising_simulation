import numpy as np
import numpy.random as npr
import math
import matplotlib.pyplot as plt

class Ising_lattice:

    def __init__(self,N,J=1.0,H=0.0):
        npr.seed(1337) #reproducibility
        self._N=N
        self._J=J
        self._H=H
        self.aligned_spins()
        self._compute_E_M()

    def aligned_spins(self,S=1):
        if (not(S==1 or S==-1)):
            print "Ising_lattice.aligned_spins: Error, spin must be +=1"
            raise(AttributeError)
        self._spins=np.ones((self._N,self._N),dtype=int)*S
        self._compute_E_M()

    def random_spins(self):
        self._spins=np.where(np.random.random((self._N,self._N))>0.5,1,-1)
        self._compute_E_M()

    def critical_temp(self):
        return (2 / (math.log(1 + math.sqrt(2))))

    # Query methods

    def N(self):
        return self._N

    def M(self):
        return self._M

    def H(self):
        return self._H

    def J(self):
        return self._J

    def E(self):
        return self._E

    def spins(self):
        return (self._spins)*1

    def spin_ij(self,i,j):
        return self._spins[i%self._N,j%self._N]

    def __str__(self):
        return '\nLattice properties: %d^2 cells, E=%f, M=%d, <E>=%f, <M>=%f\n'%\
              (self._N,self._E,self._M,self._E/self._N**2,self._M/self._N**2)

    def diagram(self):
        print self
        print np.where(self._spins>0, '@',' ')

    def picture(self):
        plt.imshow(self._spins)
        plt.show()

    def savemat(self):
        np.save("fractal", self._spins)
        print "saved"

    # Manipulation methods

    def spin_flip(self,i,j):
        N=self._N
        s=self._spins
        dM=-2.0*s[i%N,j%N]
        dE=2.0*s[i%N,j%N]*self._H
        # N==1 is a special case ... particle is it's own neighbour, so *all*
        # spins flip, self-interaction E doesn't change
        if (N>1):
            dE+=2*s[i%N,j%N]*self._J*(s[i%N,(j+1)%N]+s[(i+1)%N,j%N]+s[i%N,(j-1)%N]+s[(i-1)%N,j%N])
        self._spins[i%N,j%N]*=-1
        self._E+=dE
        self._M+=dM
        return dE

    def cond_spin_flip(self,i,j,T=None):
        if T is None:
            T = self.critical_temp()
        dE=self.spin_flip(i,j)
        if (dE<0.0 or (T>0.0 and (np.random.random()<np.exp(-dE/T)))): return dE
        self.spin_flip(i,j)
        return 0

    def mcmc(self,nflips,T=None):
        if T is None:
            T = self.critical_temp()
        for flip in xrange(nflips):
            i,j = npr.randint(self._N, size=2)
            self.cond_spin_flip(i,j,T)

  # private methods

    def _compute_E_M(self):
        self._M=np.sum(self._spins)*1.0
        self._E=0.0
        for i in range(self._N):
            for j in range(self._N):
                self._E-=self._spins[i,j]*(self._spins[i,(j+1)%self._N]+self._spins[(i+1)%self._N,j])
        self._E*=self._J
        self._E-=self._M*self._H

if __name__ == "__main__":
    a = Ising_lattice(500)
    a.random_spins()
    a.picture()
    a.mcmc(10000000)
    a.picture()
    a.savemat()
