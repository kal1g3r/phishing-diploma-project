import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# ПАРАМЕТРИ НА МОДЕЛА
# =========================================================

# Полза и разход за нападателя
G = {1: 6, 2: 8, 3: 10}   # G1, G2, G3
C = {1: 1, 2: 2, 3: 3}    # C1, C2, C3

# Базови параметри за защитника
L_base = 10   # щета при компрометиране
c = 1         # цена за проверка / време
m = 2         # цена при игнориране на легитимен имейл

# Вероятности за успех
alpha = {1: 0.05, 2: 0.10, 3: 0.15}
beta  = {1: 0.30, 2: 0.50, 3: 0.70}

# Базова стойност на p за маркиране на графиките
p_base = 0.30


# =========================================================
# ФУНКЦИИ ЗА ПОЛЕЗНОСТ
# =========================================================

def UA(p, i, j):
    """
    Полезност на нападателя.
    i = 1..3  -> S1, S2, S3
    j = 1..3  -> D1, D2, D3
    """
    if j == 1:   # D1: Игнорира
        return -p * C[i]
    elif j == 2: # D2: Отваря без клик
        return p * (alpha[i] * G[i] - C[i])
    elif j == 3: # D3: Клика / данни
        return p * (beta[i] * G[i] - C[i])
    else:
        raise ValueError("j трябва да е 1, 2 или 3")


def UD(p, i, j, L=L_base):
    """
    Полезност на потребителя (по-голямо = по-добре).
    """
    if j == 1:   # D1: Игнорира
        return -(1 - p) * m
    elif j == 2: # D2: Отваря без клик
        return -c - p * (alpha[i] * L)
    elif j == 3: # D3: Клика / данни
        return -p * (beta[i] * L)
    else:
        raise ValueError("j трябва да е 1, 2 или 3")


# =========================================================
# СМЕСЕНО РАВНОВЕСИЕ ЗА 2x2 ПОДИГРА
# Подигра: {S1, S3} x {D2, D3}
# x = P(S1), 1-x = P(S3)
# y = P(D2), 1-y = P(D3)
# =========================================================

def mixed_equilibrium_2x2(p, L=L_base):
    # Матрица на нападателя:
    #        D2      D3
    # S1    a11     a12
    # S3    a21     a22
    a11 = UA(p, 1, 2)
    a12 = UA(p, 1, 3)
    a21 = UA(p, 3, 2)
    a22 = UA(p, 3, 3)

    # Матрица на потребителя:
    #        D2      D3
    # S1    d11     d12
    # S3    d21     d22
    d11 = UD(p, 1, 2, L=L)
    d12 = UD(p, 1, 3, L=L)
    d21 = UD(p, 3, 2, L=L)
    d22 = UD(p, 3, 3, L=L)

    # y прави нападателя безразличен между S1 и S3
    # a11*y + a12*(1-y) = a21*y + a22*(1-y)
    denom_y = (a11 - a12) - (a21 - a22)
    if abs(denom_y) < 1e-12:
        y = np.nan
    else:
        y = (a22 - a12) / denom_y

    # x прави потребителя безразличен между D2 и D3
    # d11*x + d21*(1-x) = d12*x + d22*(1-x)
    denom_x = (d11 - d21) - (d12 - d22)
    if abs(denom_x) < 1e-12:
        x = np.nan
    else:
        x = (d22 - d21) / denom_x

    return x, y


# =========================================================
# 1) ЧУВСТВИТЕЛНОСТ СПРЯМО p
# =========================================================

ps = np.linspace(0.05, 0.95, 19)   # 0.05, 0.10, ..., 0.95
x_vals, y_vals, valid = [], [], []

for p in ps:
    x, y = mixed_equilibrium_2x2(p, L=L_base)
    x_vals.append(x)
    y_vals.append(y)
    valid.append(np.isfinite(x) and np.isfinite(y) and 0 <= x <= 1 and 0 <= y <= 1)

x_vals = np.array(x_vals, dtype=float)
y_vals = np.array(y_vals, dtype=float)
valid = np.array(valid, dtype=bool)

ps_v = ps[valid]
x_v = x_vals[valid]
y_v = y_vals[valid]

print("=" * 60)
print("Чувствителност спрямо p (валидни точки)")
print("=" * 60)
print("   p      P(S1)    P(S3)    P(D2)    P(D3)")
for p, x, y in zip(ps_v, x_v, y_v):
    print(f"{p:6.2f}   {x:7.3f}   {1-x:7.3f}   {y:7.3f}   {1-y:7.3f}")
print()

# ---------------------------------------------------------
# Графика 1: Нападател спрямо p
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(ps_v, x_v, marker="o", linewidth=2, label="P(S1) – Масов фишинг")
plt.plot(ps_v, 1 - x_v, marker="o", linewidth=2, label="P(S3) – Спиър-фишинг")

plt.axvline(p_base, linestyle="--", linewidth=1.5, label=f"Базов случай p = {p_base:.2f}")

plt.xlabel("p (вероятност имейлът да е фишинг)")
plt.ylabel("Вероятност за избор на стратегия")
plt.title("Смесено равновесие на нападателя спрямо p")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("attacker_equilibrium_vs_p.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------------------------------------------------------
# Графика 2: Потребител спрямо p
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(ps_v, y_v, marker="o", linewidth=2, label="P(D2) – Отваря, без клик")
plt.plot(ps_v, 1 - y_v, marker="o", linewidth=2, label="P(D3) – Клика/данни")

plt.axvline(p_base, linestyle="--", linewidth=1.5, label=f"Базов случай p = {p_base:.2f}")

plt.xlabel("p (вероятност имейлът да е фишинг)")
plt.ylabel("Вероятност за избор на стратегия")
plt.title("Смесено равновесие на потребителя спрямо p")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("defender_equilibrium_vs_p.png", dpi=300, bbox_inches="tight")
plt.show()


# =========================================================
# 2) ДОПЪЛНИТЕЛНА ЧУВСТВИТЕЛНОСТ СПРЯМО L
#    (при фиксирано p = p_base)
# =========================================================

L_values = np.linspace(2, 30, 15)   # Примерно от 2 до 30
xL_vals, yL_vals, valid_L = [], [], []

for L in L_values:
    x, y = mixed_equilibrium_2x2(p_base, L=L)
    xL_vals.append(x)
    yL_vals.append(y)
    valid_L.append(np.isfinite(x) and np.isfinite(y) and 0 <= x <= 1 and 0 <= y <= 1)

xL_vals = np.array(xL_vals, dtype=float)
yL_vals = np.array(yL_vals, dtype=float)
valid_L = np.array(valid_L, dtype=bool)

L_v = L_values[valid_L]
xL_v = xL_vals[valid_L]
yL_v = yL_vals[valid_L]

print("=" * 60)
print(f"Чувствителност спрямо L при фиксирано p = {p_base:.2f}")
print("=" * 60)
print("   L      P(S1)    P(S3)    P(D2)    P(D3)")
for L, x, y in zip(L_v, xL_v, yL_v):
    print(f"{L:6.2f}   {x:7.3f}   {1-x:7.3f}   {y:7.3f}   {1-y:7.3f}")
print()

# ---------------------------------------------------------
# Графика 3: Потребител спрямо L
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(L_v, yL_v, marker="o", linewidth=2, label="P(D2) – Отваря, без клик")
plt.plot(L_v, 1 - yL_v, marker="o", linewidth=2, label="P(D3) – Клика/данни")

plt.axvline(L_base, linestyle="--", linewidth=1.5, label=f"Базов случай L = {L_base:.0f}")

plt.xlabel("L (щета при компрометиране)")
plt.ylabel("Вероятност за избор на стратегия")
plt.title(f"Смесено равновесие на потребителя спрямо L (при p = {p_base:.2f})")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("defender_equilibrium_vs_L.png", dpi=300, bbox_inches="tight")
plt.show()


# ---------------------------------------------------------
# По желание: графика 4 – нападател спрямо L
# (обикновено ще е почти/напълно хоризонтална, но може да я запазиш)
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
plt.plot(L_v, xL_v, marker="o", linewidth=2, label="P(S1) – Масов фишинг")
plt.plot(L_v, 1 - xL_v, marker="o", linewidth=2, label="P(S3) – Спиър-фишинг")

plt.axvline(L_base, linestyle="--", linewidth=1.5, label=f"Базов случай L = {L_base:.0f}")

plt.xlabel("L (щета при компрометиране)")
plt.ylabel("Вероятност за избор на стратегия")
plt.title(f"Смесено равновесие на нападателя спрямо L (при p = {p_base:.2f})")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("attacker_equilibrium_vs_L.png", dpi=300, bbox_inches="tight")
plt.show()

print("Готово. Запазени файлове:")
print(" - attacker_equilibrium_vs_p.png")
print(" - defender_equilibrium_vs_p.png")
print(" - defender_equilibrium_vs_L.png")
print(" - attacker_equilibrium_vs_L.png")
print()

input("Натисни Enter, за да затвориш програмата...")