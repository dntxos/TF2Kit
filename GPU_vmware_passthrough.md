# Máquinas-virtuais com acesso a GPU é possível no VmWare ESXi
Caso queira utilizar ambiente virtualizado, siga os passos abaixo para habilitar 'GPU Passthrough' em sua VM.
Essas instruções são baseadas nessa discussão do fórum oficial 'Vmware Communities: https://communities.vmware.com/thread/598626

## Passo 1: Habilite o Passthrough no ESXi
Navegue no menu até “Host > Manage > Hardware” e procure pela sua placa gráfica. Selecione a sua placa gráfica e selecione “Enable Passthrough”. A máquina HOST deve pedir para reiniciar antes que possa atravessar a GPU para máquina virtual.

## Passo 2: Adicione um dispositivo PCIe na sua VM
Configure sua VM adicionando 'PCIe Device' (clicando em 'Add other Device'). Selecione sua GPU na lista de dispositivos.

## Passo 3: Desabilite o parâmetro 'Hypervisor.CPUID.v0'
É necessário para que a VM reconheça a GPU aninhada.
Para desabilitar o parâmetro, ainda na tela de configuração da VM, navegue para 'VM Options > Advanced > Edit Configurations' e adicione o seguinte parâmetro:
```
Hypervisor.CPUID.v0 = “FALSE”
```


> Observação: Não é possível utilizar dessa maneira a saída de video da GPU, apenas utilizá-la para cálculos matemáticos. Para utilizar sua saída de vídeo é necessário um emulador de display (Headless Ghost):
https://www.headlessghost.com/
