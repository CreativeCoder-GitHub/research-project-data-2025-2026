import numpy as np
from tvb.simulator.lab import *
from tvb.simulator.models.base import Model
from tvb.basic.neotraits.api import Final, List
from scipy.signal import welch

class WilsonCowanDopamine(Model):
    NO_D = 0.0
    LOW_D = 10.0
    MEDIUM_D = 25.0
    HIGH_D = 50.0

    state_variables = ['E', 'I', 'D']
    _state_variables = state_variables
    _nvar = 3
    cvar = np.array([0], dtype=np.int32)
    variables_of_interest = List(of=str, label="Variables watched by Monitors",
                                 choices=("E", "I"), default=("E", "I"))
    state_variable_range = Final(default={"E": np.array([0.0, 1.0]),
                                          "I": np.array([0.0, 1.0]),
                                          "D": np.array([0.0, 1.0])})
    
    tau_e = 10.0; tau_i = 20.0; tau_d = 100.0
    c_ee = 10.0; c_ei = 12.0; c_ie = 8.0; c_ii = 3.0
    a_e = 1.0; b_e = 2.0; a_i = 1.0; b_i = 2.0
    beta_e = 0.5; gamma_i = 0.2; k_d = 1.0

    def dfun(self, state_variables, coupling, local_coupling=0.0):
        E, I, D = state_variables
        derivative = np.empty_like(state_variables)
        S_e = (1.0 / (1.0 + np.exp(-self.a_e * ((self.c_ee*E - self.c_ei*I + coupling) - self.b_e)))) * (1 + self.beta_e*D)
        S_i = 1.0 / (1.0 + np.exp(-self.a_i * ((self.c_ie*E - self.c_ii*I + coupling) - (self.b_i + self.gamma_i*D))))
        
        derivative[0] = (-E + (1.0 - E) * S_e) / self.tau_e
        derivative[1] = (-I + (1.0 - I) * S_i) / self.tau_i
        derivative[2] = (-D + self.k_d * local_coupling) / self.tau_d
        return derivative

def run_simulation(initial_D: float, file_path: str = '.\\raw_data\\trial_new.npz'):
    conn = connectivity.Connectivity.from_file()
    conn.configure()
    n_regions = conn.number_of_regions

    cpl = coupling.Linear(a=np.array([0.02]))
    integrator = integrators.EulerStochastic(dt=0.1220703125, noise=noise.Additive(nsig=np.array([1e-4])))

    init_cond = np.zeros((1, 3, n_regions, 1))
    init_cond[0, 0, :, 0] = 25.0
    init_cond[0, 1, :, 0] = 25.0
    init_cond[0, 2, :, 0] = initial_D

    sim = simulator.Simulator(
        model=WilsonCowanDopamine(),
        connectivity=conn,
        coupling=cpl,
        integrator=integrator,
        monitors=(monitors.Raw(period=3.90625,),),
        initial_conditions=init_cond
    )
    sim.configure()

    print("Running simulation...")
    (time, data), = sim.run(simulation_length=10000.0)
    n_sensors = 64
    leadfield = np.random.randn(n_regions, n_sensors)
    sources = data[:, 0, :, 0]
    eeg_signals = sources @ leadfield 
    fs = 1000 / 0.1220703125
    frequencies, psd = welch(eeg_signals, fs=fs, nperseg=256, noverlap=128, axis=0)
    np.savez(file_path, f=frequencies, psd=psd)

for i in range(15): run_simulation(WilsonCowanDopamine.NO_D, f'.\\raw_data\\no_dopamine\\trial_{i+1}.npz')
for i in range(15): run_simulation(WilsonCowanDopamine.LOW_D, f'.\\raw_data\\low_dopamine\\trial_{i+1}.npz')
for i in range(15): run_simulation(WilsonCowanDopamine.MEDIUM_D, f'.\\raw_data\\medium_dopamine\\trial_{i+1}.npz')
for i in range(15): run_simulation(WilsonCowanDopamine.HIGH_D, f'.\\raw_data\\high_dopamine\\trial_{i+1}.npz')