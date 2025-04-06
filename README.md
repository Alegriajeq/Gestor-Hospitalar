Nome da Empresa: Clinica AGJ
MedCare - Sistema Hospitalar
Setor: Saúde
Resumo do Problema e Solução
A Clínica AGJ enfrenta dificuldades na gestão integrada de dados médicos e agendamentos devido à falta de sincronização eficiente e segura entre os sistemas. Isso resulta em gargalos operacionais, conflitos de horário e atrasos na entrega de resultados e diagnósticos, além de comprometer a segurança e eficiência, especialmente durante picos de demanda.
Solução Proposta:
A solução consiste em uma plataforma web modular, utilizando Python para o desenvolvimento da API e MySQL como banco de dados relacional. A interface será simples e funcional, com foco em acessibilidade e usabilidade. A arquitetura será planejada para permitir escalabilidade futura, com suporte a funcionalidades como agendamento , prontuários eletrônicos seguros, notificações em tempo real e upload seguro de exames. A proposta visa melhorar a eficiência, a segurança e a experiência dos usuários por meio de uma estrutura leve, segura e de fácil manutenção.
-                                              Requisitos Funcionais:
   -Cadastro de Pacientes:
O sistema deve permitir o cadastro de pacientes com informações como nome, CPF, data de nascimento, endereço, telefone, alergias e histórico médico.
O sistema deve permitir a atualização dos dados do paciente quando necessário.
  -Agendamento de Consultas:
O paciente pode agendar consultas com médicos através do sistema.
O sistema deve permitir a visualização de horários disponíveis dos médicos e permitir que o paciente escolha a especialidade.
 - Cadastro de Médicos:
O sistema deve permitir o cadastro de médicos, incluindo nome, especialidade, CRM, e horários de atendimento.
Os médicos devem ser capazes de visualizar os agendamentos de consultas e registrar os diagnósticos dos pacientes.
 - Exames e Resultados:
O sistema deve permitir o agendamento de exames (laboratoriais, de imagem, etc.).
O paciente deve poder visualizar os resultados dos exames diretamente no sistema, de forma segura.
  -Notificações e Alertas:
O sistema deve enviar notificações para pacientes e médicos sobre consultas agendadas, exames e pagamentos pendentes.
O sistema deve enviar alertas sobre datas de vencimento de prescrições médicas e necessidade de acompanhamento médico.
                             Requisitos Não Funcionais:
   -Segurança:
O sistema deve garantir a confidencialidade e integridade dos dados dos pacientes, utilizando criptografia para dados em repouso e em trânsito.
Implementar autenticação de múltiplos fatores (MFA) para acesso ao sistema.
O acesso aos prontuários médicos deve ser restrito a profissionais autorizados (médicos, enfermeiros e administradores).
 - Desempenho:
O sistema deve ser capaz de processar até 5.000 requisições simultâneas.
O tempo de resposta para acessar informações de consultas e exames deve ser inferior a 3 segundos.
   -Escalabilidade:
O sistema deve ser escalável para suportar o crescimento do hospital (aumento no número de pacientes e médicos).
O banco de dados e a infraestrutura do sistema devem ser facilmente escaláveis para atender a novas unidades hospitalares ou clínicas associadas.
   -Alta Disponibilidade:
O sistema deve ter uma disponibilidade mínima de 99,9%, com redundância de servidores e backup diário.
O sistema de recuperação de desastres deve ser implementado para garantir que os dados do paciente não sejam perdidos em caso de falhas.
   -Usabilidade:
A interface do sistema deve ser simples e intuitiva, facilitando o uso por profissionais de saúde e pacientes.
O sistema deve ser acessível para pessoas com deficiência (ex: suporte a leitores de tela).


  
