import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors
import seaborn as sns

from scipy import stats
import os

def draw(y, x, y_, x_):

    FONT_SIZE = 19
    TICKS_SIZE = 15
    LEGEND_FONT_SIZE = 12
    FIG_W = 5
    FIG_H = 4

    plt.figure(figsize=(FIG_W,FIG_H))
    plt.rc('font',family='serif')

    r_kendall, p_kendall = stats.kendalltau(y, x)
    r_spearman, p_spearman = stats.spearmanr(y, x)
    r_kendall_, p_kendall_ = stats.kendalltau(y_, x_)
    r_spearman_, p_spearman_ = stats.spearmanr(y_, x_)

    # plt.title("$\\rho$=%.3f, $\\tau$=%.3f"%(r_spearman, r_kendall), fontsize=FONT_SIZE)
    plt.title("OTCE", fontsize=FONT_SIZE)

    # set tick size 
    plt.xticks(fontsize=TICKS_SIZE)
    plt.yticks(fontsize=TICKS_SIZE)
    
    ax = sns.regplot(x,y,scatter=False)
    ax_ = sns.regplot(x_,y_,scatter=False)
           
    label_list=["ED-14-T1","ED-14-T2","NCR-14-T1", "NCR-14-T2","ED-13-T1", "ED-13-T2","NCR-13-T1", "NCR-13-T2",
                "ED-17-T1","ED-17-T2", "NCR-17-T1", "NCR-17-T2","ED-18-T1", "ED-18-T2","NCR-18-T1","NCR-18-T2",]
    selected_list=["ED-14-T2","ED-13-T2","ED-17-T2", "ED-18-T2",]
    marker_list = ['v', 'o', 'p', 'x', 's', '^']

    for i in range(len(label_list)):
        ax.scatter(x[i],y[i], alpha=0.8, s=90, label=label_list[i], marker = marker_list[0])
    for i in range(len(selected_list)):
        ax_.scatter(x_[i],y_[i], alpha=0.8, s=90, label=selected_list[i], marker = marker_list[1])
            
    # x_interval = round((max(x) - min(x)) / 3,2)
    #ax.yaxis.set_major_locator(ticker.MultipleLocator(y_interval))
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(x_interval))
    
    
    # remove spines
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax_.spines['right'].set_color('none')
    ax_.spines['top'].set_color('none')
    ax_.spines['left'].set_color('none')
    ax_.spines['bottom'].set_color('none')
    
    # grid
    ax.grid(axis='both')
    ax_.grid(axis='both')
    

    save_dir = "test"    
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    plt.savefig(os.path.join(save_dir,"OTCE.png"), bbox_inches='tight', dpi=300)
    print(r_kendall,r_spearman)
    print(r_kendall_,r_spearman_)


if __name__ == "__main__":

    y = [0.664,  0.703, 0.646,  0.660, 0.657, 0.695, 0.628, 0.683, 0.697, 0.708, 0.612, 0.681, 0.675, 0.707, 0.664, 0.666,]
    x = [-0.0380, 0.1887, 0.8990, 0.5140, 0.4142, 1.4031, 5.0050, 10.5247, 0.3525, 1.3327, 1.5211, 6.6535, 0.1070, 0.2776, 0.9038, 2.2038,]
    y_ = [0.703,0.695, 0.708, 0.707,]
    x_ = [0.1887, 1.4031, 1.3327, 0.2776,]
    o_x = [-0.0395, -0.0226, -0.0395, -0.0383, -0.0407, -0.0356, -0.0407, -0.0401, -0.0435, -0.0389, -0.0436, -0.0433, -0.0435, -0.0273, -0.0436, -0.0394,]
    o_x_ = [-0.0226, -0.0356, -0.0389, -0.0273]
    # draw(y,x,y_,x_)
    draw(y,o_x,y_,o_x_)

