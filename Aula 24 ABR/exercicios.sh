ARQUIVO="dados.csv"

echo "1. Imprimindo ID do Sensor e Local:"
awk -F, '{print $3, $4}' "$ARQUIVO"

echo -e "\n2. Excluindo a primeira linha (cabeçalho):"
sed '1d' "$ARQUIVO"

echo -e "\n3. Temperaturas maiores que 25.0 (ignorando cabeçalho):"
awk -F, 'NR>1 && $5 > 25.0' "$ARQUIVO"

echo -e "\n4. Substituindo DataCenter por Servidores:"
sed 's/DataCenter/Servidores/g' "$ARQUIVO"

echo -e "\n5. Contando leituras com status OK:"
awk -F, '$7 == "OK" {total++} END {print total}' "$ARQUIVO"

echo -e "\n6. Removendo linhas com ERRO:"
sed '/ERRO/d' "$ARQUIVO"

echo -e "\n7. Média das temperaturas:"
awk -F, 'NR>1 {soma+=$5; cont++} END {if(cont>0) print soma/cont}' "$ARQUIVO"

echo -e "\n8. Substituindo hifens das datas por barras:"
sed 's/-/\//g' "$ARQUIVO"

echo -e "\n9. Contagem de envios por sensor:"
awk -F, 'NR>1 {contagem[$3]++} END {for (sensor in contagem) print sensor, contagem[sensor]}' "$ARQUIVO"

echo -e "\n10. Substituindo CRITICO_TEMP por EMERGENCIA (imprimindo só os alterados):"
sed -n 's/CRITICO_TEMP/EMERGENCIA/p' "$ARQUIVO"

echo -e "\n11. Pipeline sed + awk (imprimindo 2ª e 5ª colunas):"
sed 's/,/ /g' "$ARQUIVO" | awk '{print $2, $5}'

echo -e "\n12. Temperatura mais alta:"
awk -F, 'NR==2 {max=$5} NR>2 {if ($5>max) max=$5} END {print max}' "$ARQUIVO"

echo -e "\n13. Adicionando [INSPECIONADO] ao sensor SNSR-01:"
sed '/SNSR-01/ s/$/ [INSPECIONADO]/' "$ARQUIVO"

echo -e "\n14. Formatando saída com printf (alinhado à esquerda):"
awk -F, 'NR>1 {printf "%-15s %s\n", $4, $6}' "$ARQUIVO"

echo -e "\n15. Soma das umidades do Armazém:"
grep "Armazém" "$ARQUIVO" | awk -F, '{soma+=$6} END {print soma}'