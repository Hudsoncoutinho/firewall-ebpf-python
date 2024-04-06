from bcc import BPF

# Carrega o programa eBPF
bpf_prog = """
#include <uapi/linux/pkt_cls.h>

BPF_HASH(counts, u32, u64, 256);

int ddos_filter(struct __sk_buff *skb) {
    u32 key = 0;
    u64 *count;

    // Incrementa o contador para o endereço IP de origem
    key = skb->pkt_type;
    count = counts.lookup_or_init(&key, &key);
    (*count)++;

    // Verifica se o número de pacotes excede o limite
    if (*count > 1000) {
        // Descarta o pacote
        return TC_ACT_SHOT;
    }

    return TC_ACT_OK;
}
"""

# Compila o programa eBPF
b = BPF(text=bpf_prog)

# Anexa o programa eBPF ao hook de filtro de pacotes
b.attach_xdp(device="eth0", fn_name="ddos_filter")
