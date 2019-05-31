from brian import *

#defaultclock.dt=0.01*ms # for a more precise picture
N=2000
tau=100*ms
freq=1/tau

eqs='''
dv/dt=(-v+a+2*sin(2*pi*t/tau))/tau : 1
a : 1
'''

neurons=NeuronGroup(N,eqs,threshold=1,reset=0)
neurons.a=linspace(2,4,N)

run(5*second,report='text') # discard the first spikes (wait for convergence)
S=SpikeMonitor(neurons)
run(5*second,report='text')

i,t=zip(*S.spikes)
plot((t % tau)/tau,i,'.')
xlabel('Spike phase')
ylabel('Parameter a')
yticks([0,N/2,N],[2,3,4])
show()
